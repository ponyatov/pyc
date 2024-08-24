## @file
## @brief `pyc` compiler

import os, sys, re

import parser

## @defgroup compiler compiler

## @brief command line processing
## @ingroup compiler
def main(argv=sys.argv):
    for sfile in sys.argv[1:]:
        with open(sfile) as src:
            parser.toks(src.read())

if __name__ == '__main__': main()

## @defgroup repl repl
## @brief REPL: Read-Eval-Print Loop
## @ingroup compiler
