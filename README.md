# Assignment 3 – VM Auto Scaling (Local → GCP)

## Setup
```bash
./setup.sh
```

## GCP CLI Install
```bash
sudo apt-get install apt-transport-https ca-certificates gnupg curl -y
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-cli -y
```

## Authentication
```bash
gcloud auth activate-service-account --key-file=gcp-key.json
gcloud config set project YOUR_PROJECT_ID
```

## Run
```bash
./run_app.sh
./run_monitor.sh
```

## Load Test
```bash
stress-ng --cpu 4 --timeout 30s
```

## Notes
- Update PROJECT_ID, ZONE, MIG_NAME in monitor.py
- Do not upload gcp-key.json to GitHub
