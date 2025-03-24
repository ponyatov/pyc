class Object:
    def __init__(self, name): self.name = name; self.nest = []

    def __truediv__(self, o): self.nest.append(o); return self

    def pad(self, depth): return ' ' * 4 * depth

    def cpp(self, depth=0):
        ret = f'{self.pad(depth)}// {self}\n'
        for i in self.nest: ret += i.cpp(depth + 1)
        return ret

    def hpp(self, depth=0): return self.cpp()

    def __repr__(self): return self.head()
    def head(self): return f'<{self.tag()}:{self.val()}>'
    def tag(self): return self.__class__.__name__.lower()
    def val(self): return f'{self.name}'
