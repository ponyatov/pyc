## @file
## @brief primitive/scalar element

from core import Object
from core.container import Tree

## @defgroup primitive primitive
## @brief primitive/scalar element
## @ingroup core

## @brief primitive/scalar element
## @ingroup primitive
class Primitive(Object):
    ## @brief most @ref primitive s return themself
    def eval(self): return self

## @brief symbol
## @ingroup primitive
class Sym(Primitive): pass

## @brief string
## @ingroup primitive
class Str(Primitive): pass

## @brief source code (string tree)
## @ingroup primitive
class S(Str, Tree): pass

## @brief generic number
## @ingroup primitive
class Num(Primitive): pass

## @brief floating point number
## @ingroup primitive
class Float(Num): pass

## @brief integer
## @ingroup primitive
class Int(Num):
    def __init__(self, V):
        match V:
            case int(V): super().__init__(V)
            case float(V): super().__init__(int(V))
            case str(V): super().__init__(int(V))
            case _: raise TypeError(type(V))

    ## @name operator

    ## @brief `+`
    def __add__(self, o):
        match o:
            case Int(): return Int(self.value + o.value)
            case _: raise TypeError(o)


## @ingroup primitive
class Hex(Int): pass

## @ingroup primitive
class Bin(Int): pass
