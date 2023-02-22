PYTHON=/usr/bin/env python

deps: requirements.txt
	pip install -r requirements.txt

docs:
	@cd docs; \
	echo "Building documentation..."; \
	pip install -r requirements.txt
	@$(PYTHON) -m mkdocs build

test:
	@$(PYTHON) -m unittest discover tests

clean:
	rm -rf venv
	find . -type f -name "*.pyc" -delete

.PHONY: init docs test