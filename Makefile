.PHONY: clean deepclean dev pre-commit lint black mypy flake8 pylint pip-check-reqs toml-sort test build upload docs

# Use pipenv when not in CI environment and pipenv command exists.
PIPRUN := $(shell [ "${CI}" != "true" ] && command -v pipenv > /dev/null 2>&1 && echo pipenv run)
PKGDIR := torchpilot

# Remove common intermediate files.
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf \
		*.egg-info \
		.coverage \
		.eggs \
		.mypy_cache \
		.pytest_cache \
		Pipfile* \
		build \
		dist \
		output \
		public

# Remove common intermediate files alongside with `pre-commit` hook and virtualenv created by `pipenv`.
deepclean: clean
	pre-commit uninstall --hook-type pre-push
	-pipenv --venv >/dev/null 2>&1 && pipenv --rm

# Prepare dev environments:
# - Install pre-commit hoook when not in CI environment.
# - Create virtual environment with pipenv and conda python when
#   - Not in CI environment.
#   - No existing venv.
#   - Conda python exists.
# - Install package in editable mode alongside with dev requirements.
dev:
	-[ "${CI}" != "true" ] && pre-commit install --hook-type pre-push
	-[ "${CI}" != "true" ] && ! pipenv --venv >/dev/null 2>&1 && [ -e /opt/conda/bin/python ] && pipenv --site-packages --python=/opt/conda/bin/python
	${PIPRUN} pip install -r requirements-dev.txt

# Run pre-commit for all files.
pre-commit:
	pre-commit run --all-files

# Lint with all tools: black, mypy, flake8, pylint and toml-sort.
lint: black mypy flake8 pylint toml-sort

# Code formatter.
black:
	${PIPRUN} python -m black setup.py tests ${PKGDIR}

# Static typing checker.
mypy:
	${PIPRUN} python -m mypy setup.py tests ${PKGDIR}

# Style checker with various of plugins.
flake8:
	${PIPRUN} python -m flake8

# Static code analysis.
# NOTE(xuan.hu): This could be simplified to pylint after pylint v2.13.0 released.
# Reference: https://github.com/PyCQA/pylint/issues/352#issuecomment-1030840822
pylint:
	${PIPRUN} python -m pylint setup.py tests ${PKGDIR}

# [Experimental] Check missing/redundant requirements.
pip-check-reqs:
	${PIPRUN} pip-missing-reqs ${PKGDIR}
	${PIPRUN} pip-extra-reqs ${PKGDIR}

# Sort and format toml files (especially for pyproject.toml).
toml-sort:
	${PIPRUN} toml-sort -a -i pyproject.toml

# Trigger tests.
test:
	${PIPRUN} python -m pytest -x -s -v --cov=${PKGDIR} --cov-fail-under=$(or $(TEST_COVERAGE_THRESHOLD),0) .

# Build package.
build:
	${PIPRUN} python -m build

# Upload package.
upload:
	${PIPRUN} python -m twine upload dist/*

# Generate docs.
docs:
	${PIPRUN} sphinx-build docs public

# Auto build docs.
devdocs:
	${PIPRUN} sphinx-autobuild docs public
