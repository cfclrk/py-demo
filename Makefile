PROJECT_DIR = src
PYPI_URL ?= https://upload.pypi.org/legacy/

.PHONY: install-dev
install-dev:
	pip install -e .[dev]

.PHONY: test
test:
	flake8 "${PROJECT_DIR}"
	mypy "${PROJECT_DIR}"
	black -q --target-version py38 --check .
	isort **/*.py --check-only
	pytest tests

.PHONY: format
format:
	black --target-version py38 "${PROJECT_DIR}"
	black --target-version py38 tests
	isort **/*.py

.PHONY: wheel
wheel:
	pip install wheel
	python setup.py bdist_wheel

.PHONY: pypi
pypi: wheel
	@echo "Deploying wheel to ${PYPI_URL}"
	pip install twine
	@twine upload \
	  -u $$PYPI_USERNAME \
	  -p $$PYPI_PASSWORD \
	  --repository-url ${PYPI_URL} \
	  dist/*.whl

.PHONY: binary
binary:
	pip install pyinstaller
	pyinstaller pyinstaller.spec

.PHONY: clean
clean:
	rm -rf build dist .mypy_cache .pytest_cache
	find -X . -name __pycache__ | xargs rm -rf
