## @file
## @brief object graph core

## @defgroup core core
## @brief object graph core

## @brief object graph root node
## @ingroup core
class Object:
    ## @name constructor

    ## create object with initial `value`
    ## @param[in] V initial `value`
    def __init__(self, V=''):
        ## @brief scalar value
        match V:
            case str(V): self.value = V
            case int(V): self.value = V
            case float(V): self.value = V
            case Object(V): raise SyntaxError(V)
            case _: raise TypeError(V, type(V))
        ## @brief ordered vector = nested elements
        self.nest = []
        ## @brief associative array = map
        self.slot = {}

    ## @name unit test

    ## @brief dump self for unit test, and compare with `mustbe`
    ## @param[in] mustbe full text @ref dump padded with `\n` and `\t`s
    def test(self, mustbe=''):
        ret = self.dump(test=True)
        match ret:
            case str(s) if s == mustbe: return True
            case _: raise AssertionError(ret)

    ## @name operators

    ## @brief iterate object thru its @ref nest ed elements
    def __iter__(self): return iter(self.nest)

    ## @brief `o[i]` operation
    def __getitem__(self, idx):
        match idx:
            case int(idx): return self.nest[idx]
            case str(udx): return self.slot[idx]
            case _: raise TypeError(idx)

    ## @brief `o[i] = some` operation
    def __setitem__(self, idx, o):
        match idx:
            case int(idx): self.nest[idx] = o
            case str(idx): self.slot[idx] = o
            case _: raise TypeError(idx)

    ## @brief // push operator
    ## @param[in] o object
    def __floordiv__(self, o):
        match o:
            case Object() as o:
                self.nest.append(o); return self
            case _: raise TypeError(type(o))

    ## @name dump/stringify
    def __repr__(self): return self.dump()

    ## @brief full test tree dump
    ## @param[in] depth current tree padding
    ## @param[in] test remove `iod` from dump (for unit tests)
    def dump(self, depth=0, test=False):
        # head
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(test)
        # nest[]ed
        for i in self.nest: ret += i.dump(depth + 1, test)
        # result
        return ret

    def head(self, test=False):
        oid = '' if test else f' @{id(self):x}'
        return f'<{self.tag()}:{self.val()}>{oid}'
    ## type/class tag
    def tag(self): return self.__class__.__name__.lower()
    ## stringed @ref value
    def val(self): return f'{self.value}'

    ## @name computation

    ## @brief evaluate object as attributed AST
    ##
    ## must raise exception as unevaluable
    ## (mostly error with undefined @ref eval () in inherited classes)
    def eval(self): raise NotImplementedError(self)
