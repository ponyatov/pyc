PY  = pyc.py frame.py
PY += hello.py

all: doxy hello.log

%.log: %.py pyc.py frame.py
	python $< > $@ && tail $(TAIL) $@
	
merge:
	git checkout master
	git checkout ponyatov -- Makefile doxy.gen $(PY)
update:
	git pull
	cd wiki ; git pull
	
NOW = $(shell date +%d%m%y)
release:
	git tag $(NOW) ; git push gh --tags

doxy: doxy.gen *.py wiki/*
	rm -rf docs ; doxygen doxy.gen 1>/dev/null
