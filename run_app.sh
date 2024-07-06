#!/usr/bin/env bash

# Local directory is SCRIPT_DIR
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    VENV_DIR="venv_linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    VENV_DIR="venv"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    VENV_DIR="venv"
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi

# Activate the virtualenv
source "$SCRIPT_DIR/$VENV_DIR/bin/activate"

# Run the app
"$SCRIPT_DIR/$VENV_DIR/bin/python" "$SCRIPT_DIR/infinite_improbability_poster.py"