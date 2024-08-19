#!/bin/bash

python3 -m venv myvenv
source myvenv/Scripts/activate
pip install -r requirements.txt
chmod +x test.sh
echo "Environment setup complete." 
