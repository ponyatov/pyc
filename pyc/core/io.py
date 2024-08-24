## @file
## @brief File I/O

## @defgroup io io
## @brief File I/O
## @ingroup core

from pyc.core import Object

## @brief I/O
## @ingroup io

class IO(Object): pass

## @brief file path
## @ingroup io
class Path(IO): pass

## @brief directory
## @ingroup io
class Dir(IO): pass

## @brief file
## @ingroup io
class File(IO): pass
