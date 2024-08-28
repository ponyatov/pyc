import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))


from core.primitive import Nil

def test_nil():
    assert Nil().test('\n<nil:>')
