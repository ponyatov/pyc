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
        with open(f'inc/{self.name}.hpp', 'w') as f: f.write(self.hpp())
        with open(f'src/{self.name}.cpp', 'w') as f: f.write(self.cpp())

pyca = Module(MODULE) / main
pyca.sync()
