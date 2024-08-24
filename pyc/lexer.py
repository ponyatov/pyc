## @file
## @brief tokenizer

from core.primitive import Int

## @defgroup lexer lexer
## @brief tokenizer
## @ingroup compiler

import ply.lex as lex

## @brief `pyc` lang tokens
## @ingroup lexer
tokens = ['nl', 'use', 'num', 'int', 'sym',
          'lp', 'rp', 'plus', 'minus', 'star', 'slash']

## drop spaces
## @ingroup lexer
t_ignore_spaces = '\s\t\r'
## '#' line comments
## @ingroup lexer
t_ignore_comment = '\#.*'

## @ingroup lexer
def t_nl(t):
    r'\n+'
    t.lineno += len(t.value)

## @ingroup lexer
t_use = 'use'

## @ingroup lexer
def t_num(t):
    r'[+\-]?[0-9]+\.[0-9]+'
    t.value = float(t.value); return t

## @ingroup lexer
def t_int(t):
    r'[+\-]?[0-9]+'
    t.value = Int(t.value); return t

## @ingroup lexer
t_lp = '\('; t_rp = '\)'

## @ingroup lexer
t_plus = '\+'; t_minus = '-'; t_star = '\*'; t_slash = '/'

## @ingroup lexer
def t_sym(t):
    r'[a-z]+'

## @ingroup lexer
def t_error(t): raise SyntaxError(t)

## @brief lexer instance
## @ingroup lexer
lexer = lex.lex()
