PYTHON=python3

deps: requirements.txt
	pip install -r requirements.txt

docs:
	cd docs; \
	echo "[*] Building Kryptoxin Documentation..."; \
	pip install -r requirements.txt --user ; \
	cd ..; \
	$(PYTHON) -m mkdocs build; \
	echo "[!] To browse local documentation, type in 'python -m mkdocs serve'"

test:
	$(PYTHON) -m unittest discover tests

install:
	$(PYTHON) setup.py install

clean:
	rm -rf venv
	find . -type f -name "*.pyc" -delete

.SILENT: docs
.PHONY: deps docs test install clean