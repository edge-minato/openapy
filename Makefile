.PHONY: install update clean build run debug test style docker
PACKAGE := $(shell grep name pyproject.toml -m1 | awk -F" " '{print $$3}')

install:
	poetry install
	poetry run pre-commit install

update:
	poetry update
	poetry run pre-commit autoupdate

clean:
	rm -rf dist && ./debug/cleanup.sh

build: clean
	poetry build

run: clean
	poetry run ${PACKAGE} generate -s "debug/apis"


debug:
	poetry run pytest ./tests -v -s -x --cov=openapy --cov-branch --durations=0 -l

test:
	poetry run tox

unittest:
	poetry run tox -e py39

quickcheck:
	poetry run pytest ./tests -x --picked -l

style:
	poetry run tox -e black,flake8,mypy,isort

docker:
	docker build . -t openapy
