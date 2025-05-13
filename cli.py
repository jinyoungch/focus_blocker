import argparse
import os
from lib import blocker, lockout

def main():
    parser = argparse.ArgumentParser(description="Focus Blocker")
    parser.add_argument("action", choices=["add", "remove", "push", "status"])
    parser.add_argument("domain", nargs="?")
    parser.add_argument("--lockout", type=int, help="Lockout period in hours")

    args = parser.parse_args()

    if args.action == "add" and args.domain:
        blocker.add_domain(args.domain)
    elif args.action == "remove" and args.domain:
        blocker.remove_domain(args.domain)
    elif args.action == "push":
        if lockout.is_locked_out():
            print("You're in a lockout period. Can't push changes.")
        else:
            blocker.push_blocklist()
            if args.lockout:
                lockout.set_lockout(args.lockout)
    elif args.action == "status":
        lockout.status()
    else:
        print("Invalid command or missing domain.")

if __name__ == "__main__":
    main()
