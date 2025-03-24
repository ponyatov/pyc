from obj import Object

class Statement(Object):
    def cpp(self, depth=0):
        return f'{self.pad(depth)}{self.tag()} {self.val()};\n'

class Return(Statement): pass
