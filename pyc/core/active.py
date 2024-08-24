## @file
## @brief EDS: Executable Data Structure

## @defgroup active active
## @brief EDS: Executable Data Structure
## @ingroup core

from core import Object

## @brief EDS: Executable Data Structure
## @ingroup active
class Active(Object): pass

## @brief operator
## @ingroup active
class Op(Active):
    def eval(self):
        match self.value:
            case '+': return self[0].eval() + self[1].eval()
            case _: raise NotImplementedError(self)
