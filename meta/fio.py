import os
from obj import *
from src import *

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

