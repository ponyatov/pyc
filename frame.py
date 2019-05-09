## @file
## @ref mmframe extended with nested elements for attribute grammar and AST processing 

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
        return self.head()
    def head(self):
        return '<%s:%s>' %(self.type,self.val)

## @}
