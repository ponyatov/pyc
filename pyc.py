## @file
## code generation engine

## @defgroup pyc pyC
## code generation engine
## @{

import os,sys

from frame import *

## software (compilation) module
class Module(Frame):
    def __init__(self,V=sys.argv[0].split('.')[0]):
        Frame.__init__(self,V)

## @}
