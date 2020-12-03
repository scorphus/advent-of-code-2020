# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

# list all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
.PHONY: list
# required for list
no_targets__:

# install dependencies and pre-commit hooks
setup:
	@PIP_REQUIRE_VIRTUALENV=true pip install -U -e .\[tests\]
	@pre-commit install -f --hook-type pre-commit
	@pre-commit install -f --hook-type pre-push
.PHONY: setup

# install dependencies
setup-ci:
	@pip install -U -e .\[tests\]
.PHONY: setup-ci

# create new challenge and tests from samples
next-day:
	@$(MAKE) new-day-$$(printf "%02d" $$(echo $$(date +%d) + 1 | bc))
.PHONY: next-day

new-day:
	@$(MAKE) new-day-$$(date +%d)
.PHONY: new-day

new-day-%:
	@cp day.py.sample aoc/day$*.py
	@cp day_test.py.sample tests/day$*_test.py
	@sed -i.tmp s/XX/$*/ tests/day$*_test.py
	@rm tests/day$*_test.py.tmp
.PHONY: new-day-

# run isort, black and flake8 for style guide enforcement
isort:
	@isort .
.PHONY: isort

black:
	@black .
.PHONY: black

flake8:
	@flake8
.PHONY: flake8

lint: isort black flake8
.PHONY: lint

# run tests with coverage
test:
	@pytest -sv --cov=aoc tests
.PHONY: test

# report coverage in html format
coverage: test
	@coverage html
.PHONY: coverage

# clean python object, test and coverage files
pyclean:
	@find . -type d -iname '__pycache__' -exec rm -rf \{\} + -print
	@find . -type d -iname '.benchmarks' -exec rm -rf \{\} + -print
	@find . -type d -iname '.mypy_cache' -exec rm -rf \{\} + -print
	@find . -type d -iname '.pytest_cache' -exec rm -rf \{\} + -print
	@find . -type d -iname '*.egg-info' -exec rm -rf \{\} + -print
	@find . -type f -iname '.coverage' -exec rm -rf \{\} + -print
	@find . -type f -name "*.pyc" -delete -print
.PHONY: pyclean
