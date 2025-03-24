
from obj import Object
from statement import Return
from typ import *

class Fn(Object):
    def __init__(self, name, retype=void):
        super().__init__(name)
        self.retype = retype
        self.weak = False

    def hpp(self):
        return f'extern {self.retype} {self.name}();\n'

    def cpp(self, depth=0):
        weak = '__attribute__((weak)) ' if self.weak else ''
        ret = f'{self.pad(depth)}{weak}{self.retype} {self.name}() {{\n'
        for i in self.nest: ret += i.cpp(depth + 1)
        ret += f'{self.pad(depth)}}}\n'
        return ret

main = Fn('main', retype=int_) / Return(0); main.weak = True
