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
    def __init__(self, path):
        self.path = path

    def __truediv__(self, o):
        o.path = f'{self.path}/{o.path}'
        return o

class Dir(IO):

    def sync(self):
        try: os.mkdir(self.path)
        except FileExistsError: pass

class File(IO):
    def __init__(self, path):
        super().__init__(path)
        self.nest = []

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
bin = Dir('bin'); bin.sync()
tmp = Dir('tmp'); tmp.sync()
((bin / File('.gitignore')) / '*').sync()
((tmp / File('.gitignore')) / '*').sync()

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

cmk = CMakeLists(); cmk.sync()
cpr = CMakePresets(); cpr.sync()

class Cross(Object):
    def __init__(self, name):
        self.name = name
        cname = self.__class__.__name__.lower()
        # cross/hw
        self.__class__.dir = Dir(cname)
        self.__class__.dir.sync()
        # cross/hw/inc
        self.__class__.dinc = self.__class__.dir / Dir('inc')
        self.__class__.dinc.sync()
        self.__class__.inc = self.__class__.dinc / File(f'{cname}.hpp')
        # cross/hw/src
        self.__class__.dsrc = self.__class__.dir / Dir('src')
        self.__class__.dsrc.sync()
        self.__class__.src = self.__class__.dsrc / File(f'{cname}.cpp')
        # (self.__class__.dir / Dir('src')).sync()
        # self.dir = self.__class__.dir / Dir(name)
        # self.dir.sync()
        # self.dinc = self.dir / Dir('inc');self.dinc.sync()
        # self.inc = self.dinc / File(f'{name}.hpp')
        # self.dsrc = self.dir / Dir('src');self.dsrc.sync()
        # self.src = self.dsrc / File(f'{name}.cpp')

    def sync(self):
        self.__class__.inc.sync()
        self.inc.sync(); self.src.sync()

class CPU(Cross):
    def sync(self):
        super().sync()

STM32L496AGI = CPU('STM32L496AGI'); STM32L496AGI.sync()

class HW(Cross):
    def __init__(self, name, cpu):
        super().__init__(name)
        self.ioc = self.dir / File(f'{name}.ioc')

    def sync(self):
        super().sync()
        # self.ioc.sync()

l496disco = HW('l496disco', cpu=STM32L496AGI); l496disco.sync()
