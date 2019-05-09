## @file
## code generation engine

## @defgroup pyc pyC
## code generation engine
## @{

import os,sys

from frame import *

## software (compilation) module
class Module(Frame):
    def __init__(self,V):
        Frame.__init__(self,V)

## GNU `Makefile`
class mkFile(File): pass

## generic C files
class cFile(File): pass

## headers file
class hFile(cFile): pass

## @}
