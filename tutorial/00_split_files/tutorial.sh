#!/bin/bash

cd `dirname $0`

. ../version.sh
docker run --rm -v "$PWD:/src" edgem/openapy:${OPENAPY_VERSION} \
openapy generate --src /src/apis

sudo chown $USER:$USER processor -R
