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
        with open(self.path, 'w') as f:
            for i in self.nest: print(i, file=f)

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

hw = Dir('hw')

class HW(Object):
    def sync(self):
        d = Dir(self.val()); hw / d
        d.sync()


for h in ['pc', 'f496disco']: HW(h).sync()
