#!/bin/bash

set -e

PYTHON35="/root/.pyenv/versions/3.5.9/bin/python3"
PYTHON36="/root/.pyenv/versions/3.6.9/bin/python3"
PYTHON37="/root/.pyenv/versions/3.7.7/bin/python3"

if [ -f "${PYTHON35}" ]; then
    echo "Building wheel for Python"
    ${PYTHON35} --version
    ${PYTHON35} setup.py bdist_wheel --plat-name=manylinux1_x86_64
fi

if [ -f "${PYTHON36}" ]; then
    echo "Building wheel for Python"
    ${PYTHON36} --version
    ${PYTHON36} setup.py bdist_wheel --plat-name=manylinux1_x86_64
fi

if [ -f "${PYTHON37}" ]; then
    echo "Building wheel for Python"
    ${PYTHON37} --version
    ${PYTHON37} setup.py bdist_wheel --plat-name=manylinux1_x86_64
fi
