from obj import *

class S(Object):
    def __init__(self, pfx=None, sfx=None):
        self.pfx = pfx; self.sfx = sfx; self.nest = []

    def gen(self, depth=0):
        def tab(depth): return ' ' * 4 * depth
        ret = ''
        if self.pfx is not None: ret += f'{tab(depth)}{self.pfx}\n'
        for i in self.nest:
            ret += i.gen(depth + 1)
        if self.sfx is not None: ret += f'{tab(depth)}{self.sfx}\n'
        return ret

    def __truediv__(self, o):
        match o:
            case o if type(o) == str: self.nest.append(S(o))
            case o if type(o) == S: self.nest.append(o)
            case _: raise TypeError(o)
        return self
