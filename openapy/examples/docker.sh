#!/bin/bash

set -eu
cd `dirname $0`

SOURCE="./src/openapi-server/apis"

function generate(){
    docker run --rm -v "$PWD:/src" edgem/openapy \
        openapy --src $SOURCE
}

function format(){
    poetry run black ./src
    poetry run isort ./src
}

generate
format
