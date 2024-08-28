import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

import parser

def test_import():
    assert parser.eval('import std').test('\n<module:std>')
