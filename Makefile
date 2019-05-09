all: hello.log doxy

%.log: %.py pyc.py
	python $< > $@ && tail $(TAIL) $@

doxy:
	rm -rf docs ; doxygen doxy.gen 1>/dev/null