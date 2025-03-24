HW = f496disco

include   hw/$(HW).mk
include  cpu/$(CPU).mk
include arch/$(ARCH).mk
include   os/$(OS).mk

.PHONY: all run
all:
run:

.PHONY: install update
install:
	$(MAKE) update
update:
	sudo apt update
	sudo apt install -uy `cat apt.$(shell lsb_release -si)` $(APT)
