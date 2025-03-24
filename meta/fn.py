
from obj import Object
from statement import Return
from typ import *

class Fn(Object):
    def __init__(self, name, retype=void):
        super().__init__(name)
        self.retype = retype

    def hpp(self):
        return f'extern {self.retype} {self.name}();\n'

    def cpp(self):
        ret = f'{self.retype} {self.name}() {{\n'
        for i in self.nest: ret += i.cpp()
        ret += '}\n'
        return ret

main = Fn('main', retype=int_) / Return(0)
