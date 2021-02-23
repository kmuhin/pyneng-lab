#!/usr/bin/env bash

. ./venv-3.9/bin/activate || exit 1
python3 -m pip --version
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python3 -m pip --version

