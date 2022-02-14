#!/bin/bash
set -e

echo "$@"

if [ $# == 0 ]; then
	openapy --version
	exit
fi

exec "$@"
