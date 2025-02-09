## @defgroup meta meta
## @{

MODULE = 'pyc'
ABOUT = 'Python/F compiler'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
LICENSE = 'MIT'

import datetime as dt
import os

YEAR = dt.date.today().year

def dirs(**kv):
    for i in ['.vscode', 'bin', 'doc', 'lib', 'inc', 'src', 'tmp', 'ref', 'hw', 'cpu', 'arch', 'os', 'meta']:
        try: os.mkdir(i)
        except FileExistsError: pass
        open(f'{i}/.gitignore', 'a').close()

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
    for component in [dirs, readme, apt]: component()
genfiles()
