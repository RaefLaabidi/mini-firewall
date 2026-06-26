from datetime import datetime
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "actions.log")

os.makedirs(LOG_FOLDER, exist_ok=True)


def log_action(action, status):
    with open(LOG_FILE, "a") as file:
        file.write(
            f"[{datetime.now()}] ACTION={action} STATUS={status}\n"
        )






