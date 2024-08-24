## @file
## @brief Networking

## @defgroup net net
## @brief Networking
## @ingroup io

## @brief networking item
## @ingroup net

from pyc.core import IO, Int, Tuple

class Net(IO): pass

## @ingroup net
class Socket(Net): pass

## @ingroup net
class TCP(Socket): pass
## @ingroup net
class UDP(Socket): pass

## @ingroup net
class Port(Net, Int): pass

## @ingroup net
class IP(Net, Tuple): pass
