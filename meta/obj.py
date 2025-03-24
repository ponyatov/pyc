class Object:
    def __init__(self, name): self.name = name; self.nest = []

    def __truediv__(self, o): self.nest.append(o); return self

    def hpp(self): return f'// {self}\n'
    def cpp(self): return f'// {self}\n'

    def __repr__(self): return self.head()
    def head(self): return f'<{self.tag()}:{self.val()}>'
    def tag(self): return self.__class__.__name__.lower()
    def val(self): return f'{self.name}'
