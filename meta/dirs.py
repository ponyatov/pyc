import os

from obj import *

DIRS = ['.', '.vscode', 'bin', 'doc', 'lib',
        'inc', 'src', 'tmp', 'ref', 'cmake',
        'hw', 'cpu', 'arch', 'os']

class Dir(Object): pass

for i in DIRS:
    try: os.mkdir(i)
    except FileExistsError: pass
    with open(f'{i}/.gitignore', 'w') as f:
        if i in ['.']: print(
            '''*~\n*.swp\n*.log\n__pycache__\n*.pyc''', file=f)
        if i in ['bin', 'ref', 'tmp']:
            print('*', file=f)
        if i in ['doc']:
            print('html/', file=f)
        print('!.gitignore', file=f)
