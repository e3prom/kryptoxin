PYTHON=python
version_file := VERSION
VERSION := $(shell cat ${version_file})

deps: requirements.txt
	${PYTHON} -m pip install -r requirements.txt

docs:
	cd docs; \
	echo "[*] Building Kryptoxin Documentation..."; \
	pip install -r requirements.txt --user ; \
	cd ..; \
	$(PYTHON) -m mkdocs build; \
	echo "[!] To browse local documentation, type in 'python -m mkdocs serve'"

test:
	$(PYTHON) -m unittest discover tests

installer:
	$(PYTHON) -m build
	$(PYTHON) -m pip install dist/kryptoxin-$(VERSION)-py3-none-any.whl

clean:
	rm -rf venv
	rm -rf build/
	rm -rf dist/
	rm -rf site/
	rm -rf kryptoxin.egg-info
	find . -type f -name "*.pyc" -delete

install: deps installer
all: deps test docs installer

.SILENT: docs
.PHONY: deps docs test install clean
