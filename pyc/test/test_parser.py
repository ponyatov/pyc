import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

import parser

def test_ast_none():
    assert parser.ast('').test('\n<nil:>')

def test_ast_int():
    assert parser.ast('01230').test('\n<int:1230>')

def test_ast_float_point():
    assert parser.ast('012.30').test('\n<float:12.3>')

def test_ast_float_exp():
    assert parser.ast('01.2e-3').test('\n<float:0.0012>')
