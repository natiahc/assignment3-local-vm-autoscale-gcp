#!/bin/bash
set -e

sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-venv stress-ng curl git apt-transport-https ca-certificates gnupg

cd "$(dirname "$0")"

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete"
echo "Run app: ./run_app.sh"
echo "Run monitor: ./run_monitor.sh"
