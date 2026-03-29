#!/bin/bash
set -e

echo "Installing Google Cloud CLI..."

sudo apt-get install -y apt-transport-https ca-certificates gnupg curl

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | \
sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt-get update
sudo apt-get install -y google-cloud-cli

echo "Authenticating..."

gcloud auth activate-service-account --key-file=gcp-key.json

echo "Setting project..."

gcloud config set project YOUR_PROJECT_ID

echo "Setup done"
