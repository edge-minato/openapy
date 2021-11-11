#!/bin/bash

RAW_GITHUB="https://raw.githubusercontent.com/OpenAPITools/openapi-generator"
OPENAPI_TAG="v5.3.0"
OPENAPI_IMAGE="openapitools/openapi-generator-cli"
GENERATOR="python-fastapi"
YAML_PATH="modules/openapi-generator/src/test/resources/3_0/petstore.yaml"
API_MUSTACHE_PATH="modules/openapi-generator/src/main/resources/${GENERATOR}/api.mustache"
APISPEC_YAML="apispec.yaml"
SERVER_DIR="server"

function clean(){
    rm -rf ${SERVER_DIR}/api/processor
}

function download_files(){
    curl -sL ${RAW_GITHUB}/${OPENAPI_TAG}/${YAML_PATH} -o apispec.yaml
    curl -sL ${RAW_GITHUB}/${OPENAPI_TAG}/${API_MUSTACHE_PATH} -o mustache/api.mustache
}

function generate(){
    docker run --rm -v ${PWD}:/local \
    ${OPENAPI_IMAGE}:${OPENAPI_TAG} generate \
    -i /local/${APISPEC_YAML} \
    -g ${GENERATOR} \
    -t /local/mustache \
    -o /local/${SERVER_DIR}
    # post process
    sudo chown minato:minato ${SERVER_DIR} -R
    #rm ${SERVER_DIR}/tests -rf
    rm ${SERVER_DIR}/src/openapi_server/processor -rf
}

#download_files
generate
