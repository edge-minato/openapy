.PHONY: install update clean build run debug test style
PACKAGE := $(shell grep name pyproject.toml -m1 | awk -F" " '{print $$3}')
VERSION := $(shell grep version pyproject.toml -m1 | awk -F" " '{print $$3}')

install:
	poetry install
	poetry run pre-commit install

update:
	poetry update
	poetry run pre-commit autoupdate

clean:
	rm -rf dist

build: clean
	poetry build

run:
	poetry run ${PACKAGE} -s "tests/server/src/openapi_server/apis" -t "testtttt"

try:
	poetry run ${PACKAGE} -s ./tests/server/src/openapi_server/apis -d ./tests -t ./tests

debug:
	poetry run pytest ./tests -s -v --openapy --cov-branch --durations=0

test:
	poetry run tox

unittest:
	poetry run tox -e py39

style:
	poetry run tox -e black,flake8,mypy,isort

doc:
	docker run --rm -v docs:/docs sphinxdoc/sphinx make html
