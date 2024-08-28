import pytest, sys

from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))

import parser

# def test_eval_int():
#     assert parser.eval('-01230') == Int(-1230)
