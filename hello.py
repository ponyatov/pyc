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

mk = mkFile('Makefile')     ; dir // mk

cc = cFile(module.val+'.c') ; dir // cc

hh = hFile(module.val+'.h') ; dir // hh

print module ; module.gen()

## @}
