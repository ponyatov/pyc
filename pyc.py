import os,sys

class Frame: pass

class Module(Frame):
    def __init__(self):
        print sys.argv[0]
        