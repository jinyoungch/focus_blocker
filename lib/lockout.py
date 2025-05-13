import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

LOCKOUT_FILE = os.getenv("LOCKOUT_FILE", "state.json")

def is_locked_out():
    if not os.path.exists(LOCKOUT_FILE):
        return False
    with open(LOCKOUT_FILE, "r") as f:
        data = json.load(f)
        return datetime.now() < datetime.fromisoformat(data["lockout_until"])

def set_lockout(hours):
    until = datetime.now() + timedelta(hours=hours)
    with open(LOCKOUT_FILE, "w") as f:
        json.dump({"lockout_until": until.isoformat()}, f)
    print(f"Lockout set until {until}")

def status():
    if not os.path.exists(LOCKOUT_FILE):
        print("No lockout active.")
        return
    with open(LOCKOUT_FILE, "r") as f:
        data = json.load(f)
        until = datetime.fromisoformat(data["lockout_until"])
        if datetime.now() < until:
            print(f"Locked out until {until}")
        else:
            print("No lockout active.")
