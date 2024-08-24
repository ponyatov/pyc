## @file
## @brief infix parser

## @defgroup parser parser
## @brief infix parser
## @ingroup compiler

from lexer import *

import ply.yacc as yacc

## @brief tokens
def toks(src):
    lexer.input(src)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok)
