#!/bin/bash

set -e

VENV_DIR=".venv"
PIP_REQUIRMENTS_PATH="modworm-sod/requirements.txt"

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

pip install -r modworm-sod/requirements.txt

npm install
npm run build

