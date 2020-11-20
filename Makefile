.PHONY: all install

all:
	@echo
	@echo "To install type 'sudo make install'"
	@echo 

install:
	@cp vreme.py ~/.local/bin/vreme
	@cp vreme.sh /usr/share/bash-completions/completions/