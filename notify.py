import argparse
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")


def send(text: str) -> bool:
    if not TOKEN or not CHAT_ID:
        print("error: TG_TOKEN or TG_CHAT_ID not set", file=sys.stderr)
        return False

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": CHAT_ID, "text": text}, timeout=10)
    return resp.ok


def main():
    parser = argparse.ArgumentParser(description="send a telegram notification")
    parser.add_argument("message", nargs="?", help="message text")
    parser.add_argument("--title", help="prepend a bold title")
    args = parser.parse_args()

    if args.message:
        text = args.message
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        parser.print_help()
        sys.exit(1)

    if args.title:
        text = f"*{args.title}*\n{text}"

    ok = send(text)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
