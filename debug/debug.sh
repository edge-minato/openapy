#!/bin/bash

cd `dirname $0` && cd ..

poetry run openapy generate -s "debug/apis"
