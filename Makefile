# tool
CURL = curl -L -o

# doc 
.PHONY: doc
doc: \
	doc/Peter_Sestoft_Programming_Language_Concepts.pdf \
	doc/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf

doc/Peter_Sestoft_Programming_Language_Concepts.pdf:
	$(CURL) $@ https://github.com/ponyatov/pyc/releases/download/init/Peter_Sestoft_Programming_Language_Concepts.pdf &

doc/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf:
	$(CURL) $@ https://github.com/ponyatov/pyc/releases/download/init/Garbage.Collection.Algorithms.for.Automatic.Dynamic.Memory.Management.pdf &

# install
.PHONY: install update ref gz
install: doc ref gz update
update:
	sudo apt update
	sudo apt install -uy `cat apt.txt`
ref:
gz:
