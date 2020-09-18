#!/bin/bash

set -e

PYTHON36="/root/.pyenv/versions/3.6.9/bin/python3"
PYTHON37="/root/.pyenv/versions/3.7.7/bin/python3"

export VERSION=2022.1
export BUILD=999

if [ -f "${PYTHON36}" ]; then
    echo "Building wheel for Python"
    ${PYTHON36} --version
    ${PYTHON36} setup.py bdist_wheel --plat-name=manylinux1_x86_64 --build=${BUILD}
fi

if [ -f "${PYTHON37}" ]; then
    echo "Building wheel for Python"
    ${PYTHON37} --version
    ${PYTHON37} setup.py bdist_wheel --plat-name=manylinux1_x86_64 --build=${BUILD}
fi
