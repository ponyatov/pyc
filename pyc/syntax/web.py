from pyc.syntax import XML, Markup, Syntax

## @brief JavaScript
## @ingroup syntax
class JS(Syntax): pass

## @brief WASM
## @ingroup syntax
class WASM(Syntax): pass

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
