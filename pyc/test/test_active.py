## @file
## @brief @ref core.Active

## @defgroup test_active active
## @ingroup test

import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

from core.primitive import Int, Sym
from core.active import Op

## @ingroup test_primitive
a = Int(123)
## @ingroup test_primitive
b = Int(456)

## @ingroup test_primitive
def test_int_literals():
    assert a.test("\n<int:123>")
    assert b.test("\n<int:456>")

## @defgroup test_op op
## @ingroup test_active

## @ingroup test_op
add = Op('+')

## @ingroup test_op
def test_op():
    assert add.test("\n<op:+>")
    ast = add // a // b
    assert ast.test("\n<op:+>\n\t<int:123>\n\t<int:456>")
    assert ast.eval().test("\n<int:579>")

## @defgroup test_cmd cmd
## @ingroup test_active

## @ingroup test_cmd
## @brief test command set available from @ref core.active.glob
def test_cmd_set():
    assert Sym('nop').eval().test('\n<cmd:nop>')
    assert Sym('halt').eval().test('\n<cmd:halt>')
