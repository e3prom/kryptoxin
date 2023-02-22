PYTHON=python3

deps: requirements.txt
	pip install -r requirements.txt

docs:
	cd docs; \
	echo "Building documentation..."; \
	pip install -r requirements.txt ; \
	cd ..; \
	$(PYTHON) -m mkdocs build

test:
	$(PYTHON) -m unittest discover tests

install:
	$(PYTHON) setup.py install

clean:
	rm -rf venv
	find . -type f -name "*.pyc" -delete

.PHONY: deps docs test install clean