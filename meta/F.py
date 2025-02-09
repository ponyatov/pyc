MODULE = 'pyc'
ABOUT = 'Python/F compiler'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
LICENSE = 'MIT'

import datetime as dt

YEAR = dt.date.today().year

def readme():
    with open('README.md', 'w') as f:
        print(f'''# ![](doc/logo.png) `{MODULE}`
## {ABOUT}\n
(c) {AUTHOR} <<{EMAIL}>> {YEAR}\n
-  github: https://github.com/ponyatov/{MODULE}
- gitflic: https://gitflic.ru/project/dponyatov/{MODULE}''', file=f)

def apt():
    with open('apt.Debian', 'w') as f:
        print('''git make curl
code meld doxygen clang-format
cmake g++ gdb flex bison libreadline-dev ragel
python3 python-ply''', file=f)

def genfiles(): readme(); apt()
genfiles()
