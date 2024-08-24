## @file
## @brief object graph core

## @defgroup core core
## @brief object graph core

## @brief object graph root node
## @ingroup core
class Object:
    ## @name constructor

    def __init__(self, V=''):
        ## @brief scalar value
        self.value = V

    ## @name dump/stringify
    def __repr__(self): return self.head()

    def head(self): return f'<{self.tag()}:{self.val()}> @{id(self):x}'
    ## type/class tag
    def tag(self): return self.__class__.__name__.lower()
    ## stringed @ref value
    def val(self): return f'{self.value}'

# import primitive
# import container
# import meta
# import io
# import net
# import ext
# import syntax
