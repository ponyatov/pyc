## @file
## @brief @ref core.Object

import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

from core import Object

def test_empty():
    assert Object().test("\n<object:>")

hello = Object('Hello')
world = Object('World')

def test_hello():
    assert hello.test("\n<object:Hello>")

def test_world():
    assert world.test("\n<object:World>")

def test_push():
    assert (hello // world).test("\n<object:Hello>\n\t<object:World>")
