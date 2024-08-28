## @file
## @brief metaprogramming

## @defgroup meta meta
## @brief metaprogramming
## @ingroup core

from core import Object

## @brief metaprogramming
## @ingroup meta
class Meta(Object): pass

## @brief module
## @ingroup meta
class Module(Meta):
    def eval(self): return self
