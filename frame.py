## @file
## @ref mmframe extended with nested elements for attribute grammar and AST processing

import os,sys 

## @defgroup frame Frame system
## @ref mmframe system
## extended with nested elements for attribute grammar and AST processing
## @{ 

## @ref mmframe extended with nested elements for attribute grammar and AST processing 
class Frame:
    ## @param[in] V frame name
    def __init__(self,V):
        ## type/class tag
        self.type = self.__class__.__name__.lower()
        ## name / boxed value in implementation language type
        self.val  = V
        ## attributes = slots = associative string-keyed array
        self.slot = []
        ## nested elements = vector = stack
        self.nest = []
        
    ## @name dump
    
    def __repr__(self):
        return self.dump()
    def dump(self,depth=0,prefix=''):
        tree = self.pad(depth) + self.head(prefix)
        for i in self.slot:
            tree += self.slot[i].dump(depth+1,prefix='%s = '%i)
        for j in self.nest:
            tree += j.dump(depth+1)
        return tree
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' %(prefix,self.type,self.val,id(self))
    def pad(self,N):
        return '\n' + '\t' * N
    
    ## @name operations
    
    def __floordiv__(self,obj):
        self.nest.append(obj) ; return self
        
    ## @name execution & code generation
    
    ## generate (to disk files)
    def gen(self,parent=None):
        for i in self.nest: i.gen()

## input/output
class IO(Frame): pass

## directory
class Dir(IO):
    ## create directory
    def gen(self,parent=None):
        try: os.mkdir(self.val)
        except OSError: pass # exits
        for i in self.nest: i.gen(parent=self)

## generic file
class File(IO):
    ## produce file
    ## @param[in] parent optional directory
    def gen(self,parent=None):
        name = self.val
        if parent: name = parent.val + '/' + name
        open(name,'w').close()
        print 'gen',name

## @}
