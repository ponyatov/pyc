PY  = pyc.py frame.py
PY += hello.py

DEMO = hello/

all: doxy hello.log

hello.log: hello.py pyc.py frame.py
	python $< > $@ && tail $(TAIL) $@
	$(MAKE) -C hello
	
merge:
	git checkout master
	git checkout ponyatov -- Makefile doxy.gen $(PY) $(DEMO)
	$(MAKE) doxy
	
update:
	git pull
	cd wiki ; git pull
	
NOW = $(shell date +%d%m%y)
release:
	git tag $(NOW) ; git push gh --tags

doxy: doxy.gen *.py wiki/*
	rm -rf docs ; doxygen doxy.gen 1>/dev/null
