## @file
## @brief @ref core.Object

import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

from core import Object

## @defgroup test_object object
## @brief @ref core.Object
## @ingroup test

## @ingroup test_object
def test_empty():
    assert Object().test("\n<object:>")

## @ingroup test_object
hello = Object('Hello')
## @ingroup test_object
world = Object('World')

## @ingroup test_object
def test_hello():
    assert hello.test("\n<object:Hello>")

## @ingroup test_object
def test_world():
    assert world.test("\n<object:World>")

## @ingroup test_object
def test_push():
    assert (hello // world).test("\n<object:Hello>\n\t<object:World>")
