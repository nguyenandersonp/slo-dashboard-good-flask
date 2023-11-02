#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed. Please install Python3."
    exit 1
fi

# Check if venv directory exists
if [ ! -d ".venv" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Run the Flask app in debug mode on 0.0.0.0
echo "Running Flask app in debug mode..."
flask --app __init__ run --host=0.0.0.0 --port=5000 --debug