#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "Starting Orange Pi Robot..."
if [ -f robot/requirements.txt ]; then
  python3 -m pip install -r robot/requirements.txt --user || true
fi
python3 run.py
