.PHONY: help format lint test serve

## help: Display this help message
help:
	@awk 'BEGIN {print "Available targets:\n"} /^## / {gsub(/^## /, ""); print "  " $$0}' $(MAKEFILE_LIST)

## format: Format Python code with ruff
format:
	uv run ruff format .

## lint: Lint Python code with ruff
lint:
	uv run ruff check . --fix

## test: Run all tests with pytest
test:
	uv run pytest

## serve: Start the FastAPI server on http://localhost:8000
serve:
	uv run python main.py

## cloc: Count lines of code
cloc:
	cloc 
