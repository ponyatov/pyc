## @file
## @brief syntax parser

import ply.lex as lex

tokens = ['nl', 'use', 'num', 'int', 'sym',
          'lp', 'rp', 'plus', 'minus', 'star', 'slash']

t_ignore_spaces = '\s\t\r'
t_ignore_comment = '\#.*'

def t_nl(t):
    r'\n+'
    t.lineno += len(t.value)

t_use = 'use'

def t_num(t):
    r'[+\-]?[0-9]+\.[0-9]+'
    t.value = float(t.value); return t

def t_int(t):
    r'[+\-]?[0-9]+'
    t.value = int(t.value); return t

t_lp = '\('; t_rp = '\)'

t_plus = '\+'; t_minus = '-'; t_star = '\*'; t_slash = '/'

def t_sym(t):
    r'[a-z]+'

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

import ply.yacc as yacc

## @brief tokens
def toks(src):
    lexer.input(src)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok)
