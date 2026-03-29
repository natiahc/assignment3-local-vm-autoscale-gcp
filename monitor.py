import time
import subprocess
import psutil

PROJECT_ID = "vcc-academic-project"
ZONE = "us-central1-a"
MIG_NAME = "burst-mig"

UPPER_LIMIT = 75
LOWER_LIMIT = 40
HIGH_HITS_NEEDED = 3
LOW_HITS_NEEDED = 2
SLEEP_SECONDS = 5
COOLDOWN_SECONDS = 60

high_hits = 0
low_hits = 0
cloud_active = False
last_action_time = 0


def resize_group(size):
    global last_action_time
    now = time.time()
    if now - last_action_time < COOLDOWN_SECONDS:
        return

    cmd = [
        "gcloud", "compute", "instance-groups", "managed", "resize", MIG_NAME,
        "--size", str(size),
        "--zone", ZONE,
        "--project", PROJECT_ID
    ]
    result = subprocess.run(cmd)
    if result.returncode == 0:
        last_action_time = now


while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"cpu={cpu:.1f}% memory={memory:.1f}%")

    if cpu >= UPPER_LIMIT or memory >= UPPER_LIMIT:
        high_hits += 1
        low_hits = 0
    elif cpu <= LOWER_LIMIT and memory <= LOWER_LIMIT:
        low_hits += 1
        high_hits = 0
    else:
        high_hits = 0
        low_hits = 0

    if high_hits >= HIGH_HITS_NEEDED and not cloud_active:
        print("Scaling out to cloud")
        resize_group(1)
        cloud_active = True
        high_hits = 0

    if low_hits >= LOW_HITS_NEEDED and cloud_active:
        print("Scaling in cloud resources")
        resize_group(0)
        cloud_active = False
        low_hits = 0

    time.sleep(SLEEP_SECONDS)
