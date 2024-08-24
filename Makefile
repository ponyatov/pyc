# tool
CURL = curl -L -o
PY   = $(which python3)
PIP  = $(which pip3)
PEP  = $(which autopep8)

# src
C += $(wildcard  src/*.c*)
H += $(wildcard  inc/*.c*)
Y += $(wildcard cmpl/*.py)

# all
.PHONY: all
all: $(C) $(H)
$(C) $(H): $(PY) $(Y)
	$^


# doc 
.PHONY: doc
doc: \
	doc/Peter_Sestoft_Programming_Language_Concepts.pdf \
	doc/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf

doc/Peter_Sestoft_Programming_Language_Concepts.pdf:
	$(CURL) $@ -sS https://github.com/ponyatov/pyc/releases/download/init/Peter_Sestoft_Programming_Language_Concepts.pdf &

doc/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf:
	$(CURL) $@ -sS https://github.com/ponyatov/pyc/releases/download/init/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf &

# install
.PHONY: install update ref gz
install: doc ref gz update
update:
	sudo apt update
	sudo apt install -uy `cat apt.txt`
ref:
gz:
