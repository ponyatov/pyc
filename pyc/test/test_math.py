import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

import parser

# def test_eval_int():
#     assert parser.eval('-01230') == Int(-1230)

def test_add_int_int():
    assert parser.eval('-01 + +03').test('\n<int:2>')
def test_sub_int_int():
    assert parser.eval('-01 - +03').test('\n<int:-4>')
def test_mul_int_int():
    assert parser.eval('-01 * +03').test('\n<int:-3>')
def test_div_int_int():
    assert parser.eval('-01 / +03').test('\n<int:0>')

def test_add_flo_flo():
    assert parser.eval('-01.20 + +03.30').test('\n<float:2.0999999999999996>')
def test_sub_flo_flo():
    assert parser.eval('-01.20 - +03.30').test('\n<float:-4.5>')
def test_mul_flo_flo():
    assert parser.eval('-01.20 * +03.30').test('\n<float:-3.9599999999999995>')
def test_div_flo_flo():
    assert parser.eval(
        '-01.20 / +03.30').test('\n<float:-0.36363636363636365>')
