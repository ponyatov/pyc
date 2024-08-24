# var
MODULE = $(notdir $(CURDIR))
PEPS   = E26,E302,E305,E401,E402,E701,E702

# dirs
CWD = $(CURDIR)

# tool
CURL = curl -L -o
PY   = $(shell which python3)
PIP  = $(shell which pip3)
PEP  = $(shell which autopep8)

# src
C += $(wildcard src/*.c*)
H += $(wildcard inc/*.c*)
Y += $(wildcard pyc/*.py) $(wildcard pyc/core/*.py) $(wildcard pyc/os/*.py)
Y += $(wildcard pyc/db/*.py) $(wildcard pyc/gui/*.py)
Y += $(wildcard pyc/game/*.py) $(wildcard pyc/cad/*.py)
Y += $(wildcard pyc/hw/*.py) $(wildcard pyc/hw/mcu/*.py)
S += $(wildcard lib/*.s*)

# all
.PHONY: all
all: $(C) $(H)
$(C) $(H): $(PY) $(MODULE)/$(MODULE).py $(S)
	$^

# format
.PHONY: format
format: tmp/format_py tmp/format_cpp
tmp/format_py: $(Y) $(S)
	$(PEP) --ignore $(PEPS) -i $? && touch $@
tmp/format_cpp: $(C) $(H)

# doc 
.PHONY: doxy
doxy: .doxygen
# $(C) $(H) $(Y) $(S) README.md
	rm -rf docs ; doxygen $< 1>/dev/null

.PHONY: doc
doc: \
	doc/Peter_Sestoft_Programming_Language_Concepts.pdf \
	doc/The_Garbage_Collection_Handbook.pdf \
	doc/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf

doc/Peter_Sestoft_Programming_Language_Concepts.pdf:
	$(CURL) $@ -sS https://github.com/ponyatov/pyc/releases/download/init/Peter_Sestoft_Programming_Language_Concepts.pdf &

doc/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf:
	$(CURL) $@ -sS https://github.com/ponyatov/pyc/releases/download/init/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf &

doc/The_Garbage_Collection_Handbook.pdf:
	$(CURL) $@ -sS https://github.com/ponyatov/pyc/releases/download/init/The_Garbage_Collection_Handbook.pdf &

# install
.PHONY: install update ref gz
install: doc ref gz update
update:
	sudo apt update
	sudo apt install -uy `cat apt.txt`
ref:
gz:
