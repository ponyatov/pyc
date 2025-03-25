## @defgroup pyc pyc
## @brief metacompiler

MODULE = 'pyc'
ABOUT = 'Python/F compiler'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
LICENSE = 'MIT'

import datetime as dt
import os as _os

YEAR = dt.date.today().year

## @defgroup object object
## @ingroup pyc
## @brief root @ref Object : common for all types

## @brief root @ref Object : common for all types
## @ingroup object
class Object:
    def __init__(self, V=None, **kv):
        self.value = V ##< scalar value: object name
        self.nest = [] ##< nested elements sub-tree = vector = stack
        self.slot = {} ##< attributes = map
        for k, v in kv.items(): self[k] = v

    ## wrap Python object into compiler class
    def _(some):
        match some:
            case Object(): return some
            case _: return Str(f'{some}')

    def __setitem__(self, k, v):
        assert isinstance(k, str)
        self.slot[k] = Object._(v)

    def tag(self): return self.__class__.__name__.lower()

    def val(self):
        if self.value is not None: return f'{self.value}'
        else: return ''

    def __repr__(self): return self.dump()

    def dump(self, depth=0, prefix=''):
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(prefix)
        for k,v in self.slot.items(): ret += v.dump(depth+1,f'{k} = ')
        return ret

    def head(self, prefix=''):
        return f'{prefix}<{self.tag()}:{self.val()}>'

    ## @brief dump compiler structure
    def sync(self): print(self)

    ## @brief `//`
    def __floordiv__(self, o):
        self.nest.append(o); return self

## @defgroup prim prim
## @ingroup object
## @brief primitive

## @brief primitive
## @ingroup prim
class Prim(Object):
    def __init__(self, V):
        super().__init__(V)
        self.pfx = [] ##< prefix strings
        self.dfx = [] ##< suffix string

## @brief source `C`ode (string tree)
## @ingroup prim
class C(Prim): pass

## @brief code section
## @ingroup prim
class S(Prim): pass
    # def __init__(self, V): super().__init__(V)

## @brief generic string
## @ingroup prim
class Str(Prim): pass

## @defgroup cont cont
## @brief container
## @ingroup object

## @brief container
## @ingroup cont
class Cont(Object): pass

## @defgroup meta meta
## @brief @ref metaprog
## @ingroup object

## @ingroup meta
class Meta(Object): pass

class Module(Meta):
    def __init__(self, V=MODULE):
        super().__init__(V, module=MODULE)

## @defgroup io io
## @brief file I/O
## @ingroup object

## @brief file I/O
## @ingroup io
class IO(Object):
    def __init__(self, name):
        self.path = [name] ##< dir/file path

## @ingroup io
class Dir(IO):
    def sync(self):
        print(f'sync: {self.path}')
        # try: _os.mkdir(self.path)
        # except FileExistsError: pass

## @ingroup io
class File(IO):
    def sync(self): self.path.sync()

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

# ## @brief regenerate project tree structure
print(Module())
