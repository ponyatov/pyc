import os, sys

MODULE = os.getcwd().split('/')[-1]

class Object: pass

class S(Object):
    def __init__(self, pfx=None, sfx=None):
        self.pfx = pfx; self.sfx = sfx
        self.nest = []

    def gen(self, depth=0):
        def tab(depth): return ' ' * 4 * depth
        ret = ''
        if self.pfx is not None: ret += f'{tab(depth)}{self.pfx}\n'
        for i in self.nest:
            ret += i.gen(depth + 1)
        if self.sfx is not None: ret += f'{tab(depth)}{self.sfx}\n'
        return ret

    def __truediv__(self, o):
        match o:
            case o if type(o) == str: self.nest.append(S(o))
            case o if type(o) == S: self.nest.append(o)
            case _: raise TypeError(o)
        return self

class IO(Object):
    def __init__(self, name):
        self.path = self.name = name
        self.nest = []

    def __truediv__(self, o):
        o.path = f'{self.path}/{o.path}'
        return o

    def __str__(self):
        return self.name

class Dir(IO):
    def __init__(self, name):
        super().__init__(name)
        self.giti = File('.gitignore'); self / self.giti

    def sync(self):
        try: os.mkdir(self.path)
        except FileExistsError: pass
        # self.giti.sync()

class File(IO):

    def sync(self):
        with open(self.path, 'w') as src:
            for i in self.nest:
                src.write(i.gen())

    def __truediv__(self, o):
        match o:
            case o if type(o) == S: self.nest.append(o)
            case o if type(o) == str: self.nest.append(S(o))
            case _: raise TypeError(o)
        return self

inc = Dir('inc'); inc.sync()
src = Dir('src'); src.sync()
bin = Dir('bin'); bin.sync(); bin.giti / '*'
tmp = Dir('tmp'); tmp.sync(); tmp.giti / '*'

hpp = inc / File(f'{MODULE}.hpp'); hpp.sync()
cpp = src / File(f'{MODULE}.cpp'); cpp.sync()

class CMakeLists(File):
    def __init__(self):
        super().__init__('CMakeLists.txt')
        self / (S()
                / 'cmake_minimum_required(VERSION 3.22)'
                / 'get_filename_component(CMAKE_PROJECT_NAME ${CMAKE_SOURCE_DIR} NAME_WE)'
                / 'project(${CMAKE_PROJECT_NAME} LANGUAGES C CXX ASM)')
        self / 'include_directories(${INC})'

        self / (S('\nfile(GLOB C', ')'))
        self / (S('\nfile(GLOB H', ')'))
        self / (S('\nfile(GLOB INC', ')'))
        self / (S('')
                / 'message("-- |")'
                / 'message("-- | app: " ${CMAKE_PROJECT_NAME})'
                / 'message("-- |")'
                )
        self / (S('\nadd_executable(${CMAKE_PROJECT_NAME}', ')')
                / '${C}  ${H}  # C/C++ source')
        self / (S('\ninstall(TARGETS ${CMAKE_PROJECT_NAME}')
                / 'DESTINATION ${CMAKE_INSTALL_PREFIX})')


class CMakePresets(File):
    def __init__(self):
        super().__init__('CMakePresets.json')
        self.common = S('{', '},') \
            / '"name"           : "common",' \
            / '"hidden"         :  true,' \
            / '"binaryDir"      : "${sourceDir}/tmp/${presetName}",' \
            / '"generator"      : "Unix Makefiles",' \
            / S('"cacheVariables" : {', '}')
        self.linux = S('{', '}') \
            / '"name"           : "linux",' \
            / '"inherits"       : "common",' \
            / S('"cacheVariables" : {', '}')
        self.configurePresets = S(
            '"configurePresets": [', ']') / self.common / self.linux
        self / (S('{', '}') / '"version": 6,' / self.configurePresets)

cmk = CMakeLists()
cpr = CMakePresets()

class Cross(Object):
    def __init__(self, name):
        self.name = name
        self.cname = self.__class__.__name__.lower()
        # cross/hw
        self.__class__.dir = Dir(self.cname)
        self.__class__.dir.sync()
        # cross/hw/inc
        self.__class__.dinc = self.__class__.dir / Dir('inc')
        self.__class__.dinc.sync()
        self.__class__.inc = self.__class__.dinc / File(f'{self.cname}.hpp')
        # cross/hw/src
        self.__class__.dsrc = self.__class__.dir / Dir('src')
        self.__class__.dsrc.sync()
        self.__class__.src = self.__class__.dsrc / File(f'{self.cname}.cpp')
        # cross/hw/cross
        self.dir = self.__class__.dir / Dir(name)
        self.dinc = self.dir / Dir('inc'); self.dinc.sync()
        self.inc = self.dinc / File(f'{name}.hpp')
        self.dsrc = self.dir / Dir('src'); self.dsrc.sync()
        self.src = self.dsrc / File(f'{name}.cpp')
        self.src / f'#include "{self.inc}"'
        # cross/hw/cross.mk
        self.mk = self.dir / File(f'{name}.mk')
        # cross/hw/cross.cmake
        self.cmake = self.dir / File(f'{name}.cmake')
        self.cmake.add_compile_options = S('add_compile_options(', ')')
        self.cmake.add_compile_definitions = S('add_compile_definitions(', ')')
        self.cmake / self.cmake.add_compile_options / \
            '' / self.cmake.add_compile_definitions

    def sync(self):
        self.__class__.inc.sync(); self.__class__.src.sync()
        self.inc.sync(); self.src.sync()
        self.mk.sync(); self.cmake.sync()

    def __str__(self):
        return self.name

class CPU(Cross):
    def sync(self):
        super().sync()

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

hw = Dir('hw'); hw.sync()
cpu = Dir('cpu'); cpu.sync()
arch = Dir('arch'); arch.sync()
oz = Dir('os'); oz.sync()

stm32l496agi = CPU('stm32l496agi'); stm32l496agi.sync()
l496disco = HW('l496disco', cpu=stm32l496agi); l496disco.sync()

i5 = CPU('i5'); i5.sync()
pc = HW('pc', cpu=i5); pc.sync()
