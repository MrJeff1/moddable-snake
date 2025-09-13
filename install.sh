#!/bin/bash
# Install dependencies (Linux/macOS)

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Installation complete. Run ./run.sh to start the game."
