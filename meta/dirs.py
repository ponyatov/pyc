import os

from obj import *

DIRS = ['.', '.vscode', 'bin', 'doc', 'lib',
        'inc', 'src', 'tmp', 'ref', 'cmake',
        'hw', 'cpu', 'arch', 'os']

class IO(Object):
    def __init__(self, name):
        super().__init__(name)
        self.path = name

class File(IO):
    def sync(self):
        with open(self.path, 'a') as f: pass
        # with open(self.path, 'w') as f:
        #     for i in self.nest: print(i, file=f)

class Dir(IO):

    def sync(self):
        try: os.mkdir(self.path)
        except FileExistsError: pass
        with open(f'{self.path}/.gitignore', 'w') as f:
            if self.name in ['.']: print(
                '''*~\n*.swp\n*.log\n__pycache__\n*.pyc''', file=f)
            if self.name in ['bin', 'ref', 'tmp']:
                print('*', file=f)
            if self.name in ['doc']:
                print('html/', file=f)
            print('!.gitignore', file=f)
        for i in self.nest: i.sync()

    def __truediv__(self, o):
        assert isinstance(o, IO)
        o.path = f'{self.path}/{o.path}'
        return super().__truediv__(o)

for i in DIRS:
    d = Dir(i)
    if i in ['hw', 'cpu', 'arch', 'os']:
        h = Dir('inc'); d / h
        (h / (File(f'{i}.hpp')
              / '#pragma once'
              / f'/// @defgroup {i} {i}' / '/// @ingroup cross'))
        c = Dir('src'); d / c
        (c / (File(f'{i}.cpp')
              / f'#include "{i}.hpp"'))
    d.sync()

class Cross(Object):
    def __init__(self, name, subdir):
        super().__init__(name)
        self.subdir = subdir

    def sync(self):
        d = Dir(self.val()); self.subdir / d
        d / File(f'{self.val()}.mk')
        d / File(f'{self.val()}.cmake')
        d.sync()

class HW(Cross):
    def __init__(self, name): super().__init__(name, Dir('hw'))

class CPU(Cross):
    def __init__(self, name): super().__init__(name, Dir('cpu'))

class ARCH(Cross):
    def __init__(self, name): super().__init__(name, Dir('arch'))

class OS(Cross):
    def __init__(self, name): super().__init__(name, Dir('os'))


for h in ['pc', 'f429disco']: HW(h).sync()
for c in ['i5', 'stm32f429zi']: CPU(c).sync()
for a in ['x86_64', 'cortexM', 'cortexM4']: ARCH(a).sync()
for s in ['bare','linux']: OS(s).sync()
