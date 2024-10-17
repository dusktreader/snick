SHELL:=/bin/bash
PACKAGE_NAME:=snick
ROOT_DIR:=$(shell dirname $(shell pwd))

.PHONY: install
install:
	poetry install

.PHONY: test
test: install
	poetry run pytest

.PHONY: mypy
mypy: install
	poetry run mypy ${PACKAGE_NAME} --pretty

.PHONY: lint
lint: install
	poetry run ruff check ${PACKAGE_NAME} tests

.PHONY: qa
qa: test lint mypy
	echo "All quality checks pass!"

.PHONY: format
format: install
	poetry run ruff format ${PACKAGE_NAME} tests

publish: install
	git tag v$(shell poetry version --short)
	git push origin v$(shell poetry version --short)

clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@rm -r .mypy_cache
	@rm -r .pytest_cache
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info
