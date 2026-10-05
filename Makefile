.PHONY: install lint test
install:
	pip install -e ".[dev,ui]"
lint:
	ruff check src tests
test:
	pytest
