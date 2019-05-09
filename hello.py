## @file
## `demo`: `Hello World`

## @defgroup demo demo

## @defgroup hello hello
## `demo`: `Hello World`
## @ingroup demo
## @{

from pyc import *

module = Module('hello')

dir = Dir(module.val)       ; module // dir

hh = hFile(module.val+'.h') ; dir // hh

cc = cFile(module.val+'.c') ; dir // cc

cc // ( '#include "' + hh.val + '"' )
cc // 'int main() {}'

hh // ( '#ifndef _H_'   + module.val )
hh // ( '#define _H_'   + module.val )
hh // ( '#endif // _H_' + module.val )

mk = mkFile('Makefile')     ; dir // mk

mk // ( '%s.exe: %s %s\n\tcc -o $@ $<' % (module.val,cc.val,hh.val) )

print module ; module.gen()

## @}
