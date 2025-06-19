import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = "trade_log.txt"

os.makedirs(LOG_DIR, exist_ok=True)

def log_action(action: str):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    line = f"[{timestamp}] ACTION: {action}\n"
    
    print(line.strip())  # Still print to console
    with open(os.path.join(LOG_DIR, LOG_FILE), "a") as f:
        f.write(line)
