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
            case '+':
                match self.nest:
                    case [unary]: return +unary.eval()
                    case [a, b]: return a.eval() + b.eval()
                    case _: raise NotImplementedError(self)
            case '-':
                match self.nest:
                    case [unary]: return -unary.eval()
                    case [a, b]: return a.eval() - b.eval()
                    case _: raise NotImplementedError(self)
            case '*':
                match self.nest:
                    case [a, b]: return a.eval() * b.eval()
                    case _: raise NotImplementedError(self)
            case '/':
                match self.nest:
                    case [a, b]: return a.eval() / b.eval()
                    case _: raise NotImplementedError(self)
            case _: raise NotImplementedError(self)
