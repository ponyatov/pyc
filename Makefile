.PHONY: install update
install:
	$(MAKE) update
update:
	sudo apt update
	sudo apt install -uy `cat apt.$(shell lsb_release -si)` $(APT)
