#!/usr/bin/env python3
"""One-line robot wedding vows — make.fun bounty entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt: exactly 116 characters, no trailing newline.
"""

import os

LINE = "I promise to love you through every firmware update, every low battery, and every reboot \u2014 until death do us unplug."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check against the bounty gate: 1-200 chars, no trailing newline.
    # Read back the bytes we just wrote and fail loudly if the gate is missed.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry length out of gate"
    assert not data.endswith(b"\n"), "entry must not end with a newline"


if __name__ == "__main__":
    main()
