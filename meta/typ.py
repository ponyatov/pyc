from obj import Object

class Type(Object):
    def cpp(self): return self.val()
    def hpp(self): return self.cpp()
    def __repr__(self): return self.val()
    
void = Type('void')
int_ = Type('int')
char = Type('char')
float = Type('float')
