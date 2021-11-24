SHELL:=/bin/bash
PACKAGE_NAME:=snick
ROOT_DIR:=$(shell dirname $(shell pwd))

install:
	poetry install

test: install
	poetry run pytest

mypy: install
	poetry run mypy ${PACKAGE_NAME} --pretty

lint: install
	poetry run black --check ${PACKAGE_NAME} tests
	poetry run isort --check ${PACKAGE_NAME} tests
	poetry run pflake8 ${PACKAGE_NAME} tests

qa: test mypy lint
	echo "All tests pass! Ready for deployment"

format: install
	poetry run black ${PACKAGE_NAME} tests
	poetry run isort ${PACKAGE_NAME} tests

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
