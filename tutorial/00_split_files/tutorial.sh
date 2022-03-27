#!/bin/bash

cd `dirname $0`

docker run --rm -v "$PWD:/src" edgem/openapy \
openapy --src /src/apis

sudo chown $USER:$USER processor -R
