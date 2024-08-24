## @file
## @brief primitive/scalar element

## @defgroup primitive primitive
## @brief primitive/scalar element
## @ingroup core

## @brief primitive/scalar element
## @ingroup primitive
class Primitive(Object): pass

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
class Int(Num): pass

## @ingroup primitive
class Hex(Int): pass

## @ingroup primitive
class Bin(Int): pass
