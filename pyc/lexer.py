## @file
## @brief tokenizer

from core.primitive import Float, Int, Sym
from core.active import Op

## @defgroup lexer lexer
## @brief tokenizer
## @ingroup compiler

import ply.lex as lex


## @brief `pyc` lang tokens
## @ingroup lexer
tokens = ['nl', 'import', 'num', 'int', 'sym',
          'lp', 'rp', 'plus', 'minus', 'star', 'slash']

## drop spaces
## @ingroup lexer
t_ignore_spaces = '\s\r'
## '#' line comments
## @ingroup lexer
t_ignore_comment = '\#.*'

## @ingroup lexer
def t_nl(t):
    r'\n+'
    t.lexer.lineno += len(t.value); return t

## @ingroup lexer
def t_import(t):
    'import\s+'
    return t

## @ingroup lexer
def t_num(t):
    r'[+\-]?[0-9]+\.[0-9]+'
    t.value = Float(t.value); return t

## @ingroup lexer
def t_int(t):
    r'[+\-]?[0-9]+'
    t.value = Int(t.value); return t

## @ingroup lexer
t_lp = '\('; t_rp = '\)'

## @ingroup lexer
def t_plus(t):
    '\+'
    t.value = Op(t.value); return t
def t_minus(t):
    '\-'
    t.value = Op(t.value); return t
def t_star(t):
    '\*'
    t.value = Op(t.value); return t
def t_slash(t):
    '\/'
    t.value = Op(t.value); return t

## @ingroup lexer
def t_sym(t):
    r'[a-z]+'
    t.value = Sym(t.value); return t

## @ingroup lexer
def t_error(t): raise SyntaxError(t)

## @brief lexer instance
## @ingroup lexer
lexer = lex.lex()
