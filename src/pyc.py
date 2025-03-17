import os, sys

MODULE = os.getcwd().split('/')[-1]

class Object: pass

class S(Object):
    def __init__(self, pfx=None, sfx=None):
        self.pfx = pfx; self.sfx = sfx
    def gen(self):
        ret = ''
        return ret

class IO(Object):
    def __init__(self, path):
        self.path = path

class Dir(IO):
    def __truediv__(self, o):
        assert type(o) == str
        return File(f'{self.path}/{o}')

    def sync(self):
        try: os.mkdir(self.path)
        except FileExistsError: pass

inc = Dir('inc'); inc.sync()
src = Dir('src'); src.sync()
bin = Dir('bin'); bin.sync()
tmp = Dir('tmp'); tmp.sync()

class File(IO):
    def __init__(self, path):
        super().__init__(path)
        self.nest = []

    def sync(self):
        with open(self.path, 'w') as src:
            for i in self.nest:
                print(i.gen(), file=src)

    def __truediv__(self, o):
        assert type(o) == S
        self.nest.append(o)

hpp = inc / f'{MODULE}.hpp'; hpp.sync()
cpp = src / f'{MODULE}.cpp'; cpp.sync()

class CMakeLists(File):
    def __init__(self): super().__init__('CMakeLists.txt')

class CMakePresets(File):
    def __init__(self):
        super().__init__('CMakePresets.json')
        self / S('{', '}')

cmk = CMakeLists(); cmk.sync()
cpr = CMakePresets(); cpr.sync()
