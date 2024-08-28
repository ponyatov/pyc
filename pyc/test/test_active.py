## @file
## @brief @ref core.Active

import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

from core import Object
from core.primitive import Int
from core.active import Op

## @defgroup test_int int
## @brief @ref Int
## @ingroup test

## @ingroup test_int
a = Int(123)
## @ingroup test_int
b = Int(456)

## @ingroup test_int
def test_int_literals():
    assert a.test("\n<int:123>")
    assert b.test("\n<int:456>")

## @defgroup test_op op
## @ingroup test

## @ingroup test_op
add = Op('+')

## @ingroup test
def test_op():
    assert add.test("\n<op:+>")
    ast = add // a // b
    assert ast.test("\n<op:+>\n\t<int:123>\n\t<int:456>")
    assert ast.eval().test("\n<int:579>")
