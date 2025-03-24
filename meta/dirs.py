import os

from obj import *

DIRS = ['.', '.vscode', 'bin', 'doc', 'lib',
        'inc', 'src', 'tmp', 'ref', 'cmake',
        'hw', 'cpu', 'arch', 'os']

class Dir(Object):
    def __init__(self, name):
        super().__init__(name)
        self.path = name

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
        assert isinstance(o, Dir)
        o.path = f'{self.path}/{o.path}'
        return super().__truediv__(o)

for i in DIRS:
    d = Dir(i)
    if i in ['hw', 'cpu', 'arch', 'os']:
        h = Dir('inc'); d / h
        c = Dir('src'); d / c
    d.sync()
