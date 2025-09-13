#!/bin/bash
# Run the moddable snake game (Linux/macOS)

# activate venv if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

exec python3 main.py
