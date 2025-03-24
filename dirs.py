import os

DIRS = ['.', '.vscode', 'bin', 'doc', 'lib', 'inc', 'src', 'tmp', 'ref']

for i in DIRS:
    try: os.mkdir(i)
    except FileExistsError: pass
    with open(f'{i}/.gitignore', 'a') as f: pass
