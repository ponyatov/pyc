## @file
## @brief input/target languages syntax & parsers

## @defgroup syntax syntax
## @brief input/target languages syntax & parsers
## @ingroup ext

from pyc.core import Meta

## @brief language syntax
## @ingroup syntax
class Syntax(Meta): pass

## @brief token lexer
## @ingroup syntax
class Lexer(Syntax): pass

## @brief @ref syntax parser
## @ingroup syntax
class Parser(Syntax): pass

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
