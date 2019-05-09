all: doxy hello.log

%.log: %.py pyc.py
	python $< > $@ && tail $(TAIL) $@
	
update:
	cd wiki ; git pull

doxy: doxy.gen *.py wiki/*
	rm -rf docs ; doxygen doxy.gen 1>/dev/null