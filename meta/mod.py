from meta import *
from obj import *
from fn import *

class Module(Object):

    def hpp(self):
        ret = '#pragma once\n'
        for i in self.nest: ret += i.hpp()
        return ret

    def cpp(self):
        ret = f'''#include "{self.name}.hpp"\n'''
        for i in self.nest: ret += i.cpp()
        return ret

    def sync(self):
        with open(f'inc/{self.name}.hpp', 'w') as f:
            print(self.hpp(), file=f)
        with open(f'src/{self.name}.cpp', 'w') as f:
            print(self.cpp(), file=f)

pyca = Module(MODULE) / main
pyca.sync()
