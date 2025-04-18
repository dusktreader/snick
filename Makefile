.ONESHELL:
.DEFAULT_GOAL:=help
SHELL:=/bin/bash
PACKAGE_TARGET:=src/snick


# ==== Helpers =========================================================================================================
.PHONY: confirm
confirm:  ## Don't use this directly
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]


.PHONY: help
help:  ## Show help message
	@awk 'BEGIN {FS = ": .*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_\/-]+(\\:[$$()% 0-9a-zA-Z_\/-]+)*:.*?##/ { gsub(/\\:/,":", $$1); printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: clean
clean:  ## Clean up build artifacts and other junk
	@rm -rf .venv
	@uv run pyclean . --debris
	@rm -rf dist
	@rm -rf .ruff_cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -f .coverage*
	@rm -f .junit.xml


# ==== Quality Control =================================================================================================
.PHONY: qa/test
qa/test:  ## Run the tests
	uv run pytest

.PHONY: qa/types
qa/types:  ## Run static type checks
	uv run mypy ${PACKAGE_TARGET} tests --pretty
	uv run basedpyright ${PACKAGE_TARGET} tests

.PHONY: qa/lint
qa/lint:  ## Run linters
	uv run ruff check ${PACKAGE_TARGET} tests
	uv run typos ${PACKAGE_TARGET} tests

.PHONY: qa/full
qa/full: qa/test qa/lint qa/types  ## Run the full set of quality checks
	@echo "All quality checks pass!"

.PHONY: qa/format
qa/format:  ## RUn code formatter
	uv run ruff format ${PACKAGE_TARGET} tests
