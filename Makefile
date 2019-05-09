all: doxy hello.log

%.log: %.py pyc.py
	python $< > $@ && tail $(TAIL) $@
	
update:
	git pull
	cd wiki ; git pull
	
NOW = $(shell date +%d%m%y)
release:
	git tag $(NOW) ; git push gh --tags

doxy: doxy.gen *.py wiki/*
	rm -rf docs ; doxygen doxy.gen 1>/dev/null