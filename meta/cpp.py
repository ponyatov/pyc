from fio import *

MODULE = os.getcwd().split('/')[-1]

hpp = inc / File(f'{MODULE}.hpp'); hpp.sync()
cpp = src / File(f'{MODULE}.cpp'); cpp.sync()
