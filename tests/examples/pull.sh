#!/bin/bash

set -eu
cd `dirname $0`

OPENAPI_TAG="v5.4.0"
APISPEC_YAML="openapi.yaml"
OWNER="OpenAPITools"
REPO="openapi-generator"

BASE_URL="https://api.github.com/repos/${OWNER}/${REPO}/contents"
FILE_PATH="modules/openapi-generator/src/main/resources/python-fastapi"
BRANCH="ref=${OPENAPI_TAG}"
URL=${BASE_URL}/${FILE_PATH}?${BRANCH}
RAW_URL="https://raw.githubusercontent.com/${OWNER}/${REPO}/${OPENAPI_TAG}/${FILE_PATH}"


mkdir mustache/${OPENAPI_TAG} -pv
curl -sL ${RAW_URL}/api.mustache > mustache/${OPENAPI_TAG}/api.mustache
