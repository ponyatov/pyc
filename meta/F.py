## @defgroup meta meta
## @{

MODULE = 'pyc'
ABOUT = 'Python/F compiler'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
LICENSE = 'MIT'

import datetime as dt

YEAR = dt.date.today().year

def readme(**kv):
    with open('README.md', 'w') as f:
        print(f'''# ![](doc/logo.png) `{MODULE}`
## {ABOUT}\n
(c) {AUTHOR} <<{EMAIL}>> {YEAR}\n
-  github: https://github.com/ponyatov/{MODULE}
- gitflic: https://gitflic.ru/project/dponyatov/{MODULE}''', file=f)

def apt(cortex=False, **kv):
    with open('apt.Debian', 'w') as f:
        print('''git make curl
code meld doxygen clang-format
cmake g++ gdb flex bison libreadline-dev ragel''', file=f)
        if cortex:
            print('''gcc-arm-none-eabi gdb-multiarch qemu-system-arm newlib-source stlink-tools dfu-util''', file=f)
        print('''python3 python3-ply''', file=f)

## @brief regenerate file tree structure
def genfiles():
    for component in [readme, apt]: component(cortex=True)
genfiles()
