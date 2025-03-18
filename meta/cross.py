import re
from obj import *
from fio import *

hw = Dir('hw'); hw.sync()
cpu = Dir('cpu'); cpu.sync()
arch = Dir('arch'); arch.sync()
oz = Dir('os'); oz.sync()

class Cross(Object):
    def __init__(self, name, cdef=[], copt=[], clink=[], **kw):
        self.name = name
        self.cname = self.__class__.__name__.lower()
        # cross/hw
        self.__class__.dir = Dir(self.cname)
        self.__class__.dir.sync()
        # cross/hw/inc
        self.__class__.dinc = self.__class__.dir / Dir('inc')
        self.__class__.dinc.sync()
        self.__class__.hpp = (File(f'{self.cname}.hpp')
                              / f'/// @defgroup {self.cname} {self.cname}'
                              / f'/// @ingroup cross')
        self.__class__.inc = self.__class__.dinc / self.__class__.hpp
        # cross/hw/src
        self.__class__.dsrc = self.__class__.dir / Dir('src')
        self.__class__.dsrc.sync()
        self.__class__.cpp = (File(f'{self.cname}.cpp')
                              / f'#include "{self.cname}.hpp"')
        self.__class__.src = self.__class__.dsrc / self.__class__.cpp
        # cross/hw/cross
        self.dir = self.__class__.dir / Dir(name); self.dir.sync()
        self.dinc = self.dir / Dir('inc'); self.dinc.sync()
        self.inc = self.dinc / File(f'{name}.hpp')
        self.dsrc = self.dir / Dir('src'); self.dsrc.sync()
        self.src = self.dsrc / File(f'{name}.cpp')
        self.src / f'#include "{self.inc}"'
        # cross/hw/cross.mk
        self.mk = self.dir / File(f'{name}.mk')
        # cross/hw/cross.cmake
        self.cmake = self.dir / File(f'{name}.cmake')
        self.cmake.kw = S('', '')
        self.cmake.add_compile_options = S('add_compile_options(', ')')
        self.cmake.add_compile_definitions = S('add_compile_definitions(', ')')
        self.cmake.add_link_options = S('add_link_options(', ')')
        self.cmake / self.cmake.kw / self.cmake.add_compile_options / \
            '' / self.cmake.add_compile_definitions / \
            '' / self.cmake.add_link_options
        # cmake
        try:
            for k, v in kw['kw'].items(): self.cmake.kw / f'set({k} {v})'
        except KeyError: pass
        for i in copt: self.cmake.add_compile_options / i
        for j in cdef: self.cmake.add_compile_definitions / j
        for k in clink: self.cmake.add_link_options / k

    def sync(self):
        self.__class__.inc.sync(); self.__class__.src.sync()
        self.inc.sync(); self.src.sync()
        self.__class__.dinc.giti.sync(); self.__class__.dsrc.giti.sync()
        self.dinc.giti.sync(); self.dsrc.giti.sync()
        self.mk.sync(); self.cmake.sync()

    def __str__(self):
        return self.name

class CPU(Cross):
    def __init__(self, name, arch, cdef=[], copt=[]):
        super().__init__(name, cdef=cdef, copt=copt)
        (self.inc
         / f'#pragma once'
         / f'/// @defgroup {name} {name}'
         / f'/// @ingroup {arch}'
         / '/// @{' / '/// @}'
         )
        self.mk / f'ARCH = {arch}'

    def sync(self):
        super().sync()

class OS(Cross):
    def __init__(self, name):
        super().__init__(name)
        (self.inc
         / f'#pragma once'
         / f'/// @defgroup {name} {name}'
         / f'/// @ingroup os'
         / '/// @{' / '/// @}'
         )

class ARCH(Cross):
    def __init__(self, name, os, cdef=[], copt=[], clink=[], **kw):
        super().__init__(name, cdef=cdef, copt=copt, clink=clink, kw=kw)
        ingroup = 'cortexM' if re.match(r'cortexM\d+', name) else 'arch'
        (self.inc
         / f'#pragma once'
         / f'/// @defgroup {name} {name}'
         / f'/// @ingroup {ingroup}'
         / '/// @{' / '/// @}'
         )
        if re.match(r'^cortexM$', name):
            (self.mk
             / 'OS     = bare'
             / 'TARGET = arm-none-eabi'
             / 'EXE    = .elf'
             / 'APT   += gcc-$(TARGET)   gdb-multiarch'
             / 'APT   += qemu-system-arm newlib-source'
             / 'APT   += stlink-tools dfu-util dos2unix')
        if re.match(r'^cortexM\d+$', name):
            self.mk / 'include arch/cortexM/cortexM.mk'
            self.cmake.nest.insert(0, S('include(arch/cortexM/cortexM.cmake)'))

class HW(Cross):
    def __init__(self, name, cpu):
        super().__init__(name)
        self.ioc = self.dir / File(f'{name}.ioc')
        self.gdb = self.dir / File(f'{name}.gdb')
        self.ocd = self.dir / File(f'{name}.ocd')
        (self.inc
         / f'#pragma once'
         / f'/// @defgroup {name} {name}'
         / f'/// @ingroup {self.cname}'
         / f'/// @brief `cpu: ` @ref {cpu}'
         / '/// @{' / '/// @}'
         )
        self.mk / f'CPU = {cpu}'

    def sync(self):
        super().sync()
        # self.gdb.sync(); self.ocd.sync()

bare = OS('bare'); bare.sync()
linux = OS('linux'); linux.sync()

x86_64 = ARCH('x86_64', os=linux); x86_64.sync()
cortexM = ARCH('cortexM', os=bare,
               cdef=['USE_HAL_DRIVER'], copt=['-mthumb']); cortexM.sync()
cortexM4 = ARCH('cortexM4', os=bare,
                copt=['${MCPU} ${MFPU}'], clink=['${MCPU} ${MFPU}'],
                MCPU='-march=armv7e-m   -mcpu=cortex-m4',
                FCPU='-mfpu=fpv4-sp-d16 -mfloat-abi=hard'); cortexM4.sync()
cortexM4.mk / 'include arch/cortexM/cortexM.mk'

stm32l496agi = CPU('stm32l496agi', arch=cortexM4,
                   cdef=['STM32L496xx']); stm32l496agi.sync()
l496disco = HW('l496disco', cpu=stm32l496agi); l496disco.sync()

i5 = CPU('i5', arch=x86_64); i5.sync()
pc = HW('pc', cpu=i5); pc.sync()
