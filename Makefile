# Phony targets for cleanliness
.PHONY: install

install:
	pip install -e .

requirements.txt: requirements.in     ## rebuild requirements.txt from requirements.in (requires: pip install pip-tools)
	pip install pip-tools
	pip-compile --output-file $@ $<
