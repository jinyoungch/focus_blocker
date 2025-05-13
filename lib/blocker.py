import os
import requests
from dotenv import load_dotenv

load_dotenv()

BLOCKLIST_FILE = os.getenv("BLOCKLIST_FILE", "blocklist.txt")
API_KEY = os.getenv("NEXTDNS_API_KEY")
PROFILE_ID = os.getenv("NEXTDNS_PROFILE_ID")

def read_blocklist():
    if not os.path.exists(BLOCKLIST_FILE):
        return []
    with open(BLOCKLIST_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def write_blocklist(domains):
    with open(BLOCKLIST_FILE, "w") as f:
        f.write("\n".join(domains))

def add_domain(domain):
    domains = read_blocklist()
    if domain not in domains:
        domains.append(domain)
        write_blocklist(domains)
        print(f"Added {domain} to blocklist.")

def remove_domain(domain):
    domains = read_blocklist()
    if domain in domains:
        domains.remove(domain)
        write_blocklist(domains)
        print(f"Removed {domain} from blocklist.")

def push_blocklist():
    headers = {"Authorization": f"token {API_KEY}"}
    url = f"https://api.nextdns.io/profiles/{PROFILE_ID}/denylists"
    domains = read_blocklist()

    # Clear existing denylist (for simplicity)
    requests.delete(url, headers=headers)

    for domain in domains:
        response = requests.post(url, headers=headers, json={"domain": domain})
        print(f"Pushed {domain}: {response.status_code}")
