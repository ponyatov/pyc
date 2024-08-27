## @file
## @brief infix parser

## @defgroup parser parser
## @brief infix parser
## @ingroup compiler

from lexer import tokens, lexer
from core.meta import Module

import ply.yacc as yacc

precedence = (
    ('left', 'plus', 'minus'),
    ('left', 'star', 'slash'),
)

def p_syntax_none(p):
    ' syntax : '
    pass
def p_syntax_recur(p):
    ' syntax : syntax ex '
    if p[2]: print(p[2])

def p_ex_nl(p):
    ' ex : nl '
    pass

def p_ex_parens(p):
    ' ex : lp ex rp '
    p[0] = p[2]
def p_ex_int(p):
    ' ex : int '
    p[0] = p[1]
def p_ex_num(p):
    ' ex : num '
    p[0] = p[1]

def p_ex_import(p):
    ' ex : import sym'
    p[0] = Module(p[2].val())
def p_ex_sym(p):
    ' ex : sym '
    p[0] = p[1]

def p_ex_add(p):
    ' ex : ex plus ex '
    p[0] = p[2] // p[1] // p[3]
def p_ex_sub(p):
    ' ex : ex minus ex '
    p[0] = p[2] // p[1] // p[3]
def p_ex_mul(p):
    ' ex : ex star ex '
    p[0] = p[2] // p[1] // p[3]
def p_ex_div(p):
    ' ex : ex slash ex '
    p[0] = p[2] // p[1] // p[3]

def p_error(p): raise SyntaxError(p)

parser = yacc.yacc(debug=False, write_tables=False)

## @brief print tokens
## @param[in] src source code
def toks(src):
    lexer.input(src)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok)

## @brief ast parsing
## @param[in] src source code
def ast(src):
    return parser.parse(src, tracking=True)
