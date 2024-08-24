# tool
CURL = curl -L -o
PY   = $(shell which python3)
PIP  = $(shell which pip3)
PEP  = $(shell which autopep8)

# src
C += $(wildcard  src/*.c*)
H += $(wildcard  inc/*.c*)
Y += $(wildcard cmpl/*.py)
S += $(wildcard  lib/*.s*)

# all
.PHONY: all
all: $(C) $(H)
$(C) $(H): $(PY) $(Y) $(S)
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
