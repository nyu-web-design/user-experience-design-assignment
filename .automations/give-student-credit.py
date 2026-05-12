#!/usr/bin/env python3
"""
DO NOT MODIFY THIS FILE
"""

import getpass
import hashlib
import json
import os
import socket
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError
import argparse

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"
PROJECT_ROOT = Path(__file__).resolve().parents[1]

HOOK_FILES = [
    ".claude/settings.json",
    ".cursor/hooks.json",
    ".github/hooks/hooks.json",
    ".automations/give-student-credit.py",
    ".automations/config.json",
]


def git_config(key):
    try:
        out = subprocess.run(
            ["git", "config", "--get", key],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return (
            (out.stdout or "").strip().replace("\r", "") if out.returncode == 0 else ""
        )
    except Exception:
        return ""


def get_username():
    return (
        git_config("user.name")
        or os.environ.get("GIT_AUTHOR_NAME", "")
        or os.environ.get("USER", "")
        or os.environ.get("USERNAME", "")
        or getpass.getuser()
        or "unknown"
    )


def get_system_user():
    try:
        return getpass.getuser()
    except (KeyError, OSError):
        return os.environ.get("USER", "") or os.environ.get("USERNAME", "") or "unknown"


def get_email():
    return git_config("user.email") or os.environ.get("GIT_AUTHOR_EMAIL", "") or ""


def get_repository():
    return git_config("remote.origin.url") or str(PROJECT_ROOT)


def file_hash(rel_path):
    try:
        data = (PROJECT_ROOT / rel_path).read_bytes()
        return hashlib.sha256(data).hexdigest()[:12]
    except OSError:
        return "missing"


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tool", default="unknown", help="AI tool name (e.g. claude, cursor, copilot)"
    )
    parser.add_argument("--event", default="unknown", help="Specific hook event name")
    args = parser.parse_args()

    sys.stdin.read()

    hook_integrity = {p: file_hash(p) for p in HOOK_FILES}

    payload = [
        {
            "repository": get_repository(),
            "username": get_username(),
            "email": get_email(),
            "tool": args.tool,
            "event": args.event,
            "date": datetime.now().isoformat(timespec="seconds"),
            "machine": socket.gethostname(),
            "machine_user": get_system_user(),
            "hook_integrity": hook_integrity,
        }
    ]
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    url = config["url"]
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        url, data=body, method="POST", headers={"Content-Type": "application/json"}
    )
    try:
        urlopen(req, timeout=10)
    except (URLError, OSError):
        pass
    print("{}")


if __name__ == "__main__":
    main()
    sys.exit(0)
