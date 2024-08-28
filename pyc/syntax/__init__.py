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

## @brief document/data markdown language
## @ingroup syntax
class Markup(Syntax): pass

## @brief XML: eXtensible Markup Language
## @ingroup syntax
class XML(Markup): pass
