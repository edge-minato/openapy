#!/bin/bash

set -eu
cd `dirname $0`

OPENAPI_IMAGE_TAG="v5.4.0"
OPENAPI_TAG="custom"
OPENAPI_IMAGE="openapitools/openapi-generator-cli"
GENERATOR="python-fastapi"
APISPEC_YAML="openapi_${OPENAPI_TAG}.yaml"

function generate(){
    docker run --rm -v ${PWD}:/local \
    ${OPENAPI_IMAGE}:${OPENAPI_IMAGE_TAG} generate \
    -i /local/${APISPEC_YAML} \
    -g ${GENERATOR} \
    -t /local/mustache/${OPENAPI_TAG} \
    -o /local/apis/tmp
    sudo chown ${USER}:${USER} apis/tmp/src/openapi_server/apis -R
    mkdir -pv apis/${OPENAPI_TAG}
    sudo mv apis/tmp/src/openapi_server/apis/* apis/${OPENAPI_TAG}
    sudo rm -rf apis/tmp
}

function format(){
    poetry run black src
}


generate
#format