PROJECT_NAME=fib
OK_MSG = \x1b[32m ✔\x1b[0m

# Set the limit for when coverage fails
COVERAGE_LIMIT=100

# Directories containing python code
CODE_LOCATIONS=$(PROJECT_NAME) tests

SHELL=bash

.venv: requirements.txt test_requirements.txt
	test -d .venv || python3 -m venv .venv
	source .venv/bin/activate
	.venv/bin/pip install -r test_requirements.txt
	touch .venv

flake: .venv
	@echo -n "==> Running flake8..."
	@flake8 --show-source  --statistics --max-complexity=10 --max-line-length=120 $(CODE_LOCATIONS)
	@echo -e "$(OK_MSG)"

unittests: .venv
	@echo -n "==> Running tests..."
	@PYTHONPATH=. .venv/bin/pytest tests --cov-report term-missing:skip-covered --cov $(PROJECT_NAME) --no-cov-on-fail --cov-fail-under=$(COVERAGE_LIMIT) -W ignore::DeprecationWarning -v
	@echo -e "$(OK_MSG)"

testformatting: .venv
	@echo -n "==> Checking that code is autoformatted with black..."
	@.venv/bin/black --check $(CODE_LOCATIONS)
	@echo -e "$(OK_MSG)"

testtyping:
	@echo -n "==> Type checking..."
	@.venv/bin/mypy -p $(PROJECT_NAME)

echostarttest:
	@echo -e "Checking the hyperdrive..."

test: echostarttest unittests testformatting testtyping flake
	@echo -e "It's a go captain $(OK_MSG)"

clean:
	rm -rf .venv



