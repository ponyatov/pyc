import os, sys

MODULE = os.getcwd().split('/')[-1]

class Object: pass

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
    def sync(self):
        with open(self.path, 'w') as src: pass

hpp = inc / f'{MODULE}.hpp'; hpp.sync()
cpp = src / f'{MODULE}.cpp'; cpp.sync()

cmk = File('CMakeLists.txt'); cmk.sync()
cpr = File('CMakePresets.json'); cpr.sync()
