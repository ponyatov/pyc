## @file
## @brief data collection

## @defgroup container container
## @brief data collection
## @ingroup core

from core import Object

## @brief data collection
## @ingroup container
class Container(Object): pass

## @brief fixed-size tuple (short vector)
## @ingroup container
class Tuple(Container): pass


## @brief ordered list
## @ingroup container
class List(Container): pass

## @brief associative array
## @ingroup container
class Map(Container): pass

## @brief LIFO
## @ingroup container
class Stack(Container): pass

## @brief FIFO
## @ingroup container
class Queue(Container): pass


## @brief tree
## @ingroup container
class Tree(Container): pass
