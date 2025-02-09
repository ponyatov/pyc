## @defgroup meta meta
## @{

MODULE = 'pyc'
ABOUT = 'Python/F compiler'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
LICENSE = 'MIT'

import datetime as dt
import os as _os

YEAR = dt.date.today().year

def dirs(**kv):
    d = ['.', '.vscode', 'bin', 'doc', 'lib',
         'inc', 'src', 'tmp', 'ref', 'meta']
    f = map(lambda i: f'{i}/.gitignore', d)
    for i in d:
        try: _os.mkdir(i)
        except FileExistsError: pass
    map(lambda i: open(i, 'a').close(), f)

def giti(**kv):
    with open('.gitignore', 'w') as i:
        print('''*~\n*.swp\n*.log\n!.gitignore''', file=i)
    with open('.gitattributes', 'w') as j:
        print('* text=auto eol=lf', file=j)
        print('\n# All source code in UNIX format', file=j)
        for e in ['c', 'cpp', 'h', 'hpp', 's', 'ld']:
            print(f'*.{e:3} text diff=cpp', file=j)
        print('\n# Binary files', file=j)
        for b in ['bin', 'elf', 'dfu', 'png', 'pdf', 'doc', 'docx']:
            print(f'*.{b:4} binary', file=j)
        print('\n# Linux', file=j)
        for l in ['sh', 'rc', 'service']:
            print(f'*.{l:7} text eol=lf', file=j)
        print('\n# Windows/MSYS', file=j)
        for w in ['bat', 'ps*']:
            print(f'*.{w} text eol=crlf', file=j)

def hw(**kv):
    d = ['hw', 'hw/inc', 'hw/src']
    try:
        for j in d: _os.mkdir(j); open(f'{j}/.gitignore', 'a')
    except FileExistsError: pass

def cpu(**kv):
    d = 'cpu'
    try:
        _os.mkdir(d)
        for s in ['inc', 'src']:
            _os.mkdir(f'{d}/{s}')
    except FileExistsError: pass

def arch(**kv):
    d = 'arch'
    try:
        _os.mkdir(d)
        for s in ['inc', 'src']:
            _os.mkdir(f'{d}/{s}')
    except FileExistsError: pass

def os(**kv):
    d = 'os'
    try:
        _os.mkdir(d)
        for s in ['inc', 'src']:
            _os.mkdir(f'{d}/{s}')
    except FileExistsError: pass
def cross(**kv):
    hw(**kv); cpu(**kv); arch(**kv); os(**kv)

def readme(**kv):
    with open('README.md', 'w') as f:
        print(f'''# ![](doc/logo.png) `{MODULE}`
## {ABOUT}\n
(c) {AUTHOR} <<{EMAIL}>> {YEAR}\n
-  github: https://github.com/ponyatov/{MODULE}
- gitflic: https://gitflic.ru/project/dponyatov/{MODULE}''', file=f)

def apt(cortex=True, win32=False, mingw64=False, **kv):
    with open('apt.Debian', 'w') as f:
        print('''git make curl
code meld doxygen clang-format
cmake g++ gdb flex bison libreadline-dev ragel
python3 python3-venv python3-ply''', file=f)
        if cortex:
            print('''gcc-arm-none-eabi    gdb-multiarch qemu-system-arm newlib-source stlink-tools dfu-util dos2unix''', file=f)
        if win32:
            print('''g++-mingw-w64-i686                 wine32''', file=f)
        if mingw64:
            print('''g++-mingw-w64-x86-64 gdb-mingw-w64 wine64 wine64-tools''', file=f)

## @brief regenerate file tree structure
def genfiles():
    for component in [dirs, giti, cross, readme, apt]: component()
genfiles()
