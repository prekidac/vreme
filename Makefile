.PHONY: all install

all:
	@echo
	@echo "To install type 'sudo make install'"
	@echo 

install:
	@chmod +x vreme.py
	@cp vreme.py /usr/local/bin/vreme
	@cp vreme.sh /usr/share/bash-completion/completions/vreme
