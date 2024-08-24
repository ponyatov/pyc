## @file
## @brief object graph core

## @defgroup core core
## @brief object graph core

## @brief object graph root node
## @ingroup core
class Object: pass

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

## @defgroup container container
## @brief data collection
## @ingroup core

## @brief data collection
## @ingroup container
class Container(Object): pass

## @brief fixed-size tuple (short vector)
## @ingroup container
class Tuple(Container): pass

## @brief ordered list
## @ingroup container
class List(Container): pass

## @brief associative array
## @ingroup container
class Map(Container): pass

## @brief LIFO
## @ingroup container
class Stack(Container): pass

## @brief FIFO
## @ingroup container
class Queue(Container): pass

## @brief tree
## @ingroup container
class Tree(Container): pass

## @defgroup meta meta
## @brief metaprogramming
## @ingroup core

## @brief metaprogramming
## @ingroup meta
class Meta(Object): pass

import syntax


## @brief ANSI C
## @ingroup syntax
class C(Syntax): pass

## @brief C++
## @ingroup syntax
class Cpp(C): pass

## @brief JavaScript
## @ingroup syntax
class JS(Syntax): pass

## @brief WASM
## @ingroup syntax
class WASM(Syntax): pass

## @brief document/data markdown language
## @ingroup syntax
class Markup(Syntax): pass

## @brief document language
## @ingroup syntax
class Markdown(Markup): pass

## @brief diagram language
## @ingroup syntax
class Mermaid(Markup): pass

## @brief JSON: JavaScript Object Notation
## @ingroup syntax
class JSON(Markup): pass

## @brief CSS: Cascading Style Sheets
## @ingroup syntax
class CSS(Markup): pass

## @brief HTML: HyperText Markdown Language
## @ingroup syntax
class HTML(XML): pass

## @brief SVG: Scalable Vector Graphics
## @ingroup syntax
class SVG(XML): pass

## @brief XML: eXtensible Markup Language
## @ingroup syntax
class XML(Markup): pass

## @brief GNU `make`
## @ingroup syntax
class Makefile(Syntax): pass

import io
import net
import ext
