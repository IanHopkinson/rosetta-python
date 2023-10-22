SHELL := /bin/bash
.PHONY: docs

install:
	pip install -e .
unit_tests:
	 python -m unittest -v
lint:
	black . --check
	flake8 src/ tests/
	pylint src/ tests/ || true
docs:
	sphinx-apidoc -o docs/source/ src
	$(MAKE) -C docs/ html
	



