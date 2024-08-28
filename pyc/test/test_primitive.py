## @file
## @brief primitives

## @defgroup test_primitive primitive
## @ingroup test

import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

from core.primitive import Nil, Sym

def test_nil():
    assert Nil().test('\n<nil:>')

def test_sym():
    assert Sym('nop').eval().test('\n<cmd:nop>')
    assert Sym('halt').eval().test('\n<cmd:halt>')
