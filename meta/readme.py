from meta import *

class Readme:
    def sync(self):
        with open('README.md', 'w') as f:
            print(f'''# `{MODULE}`
## {TITLE}

(c) {AUTHOR} <<{EMAIL}>> {YEAR} {LICENSE}

github: https://github.com/ponyatov/{MODULE.lower()}''', file=f)

readme = Readme(); readme.sync()
