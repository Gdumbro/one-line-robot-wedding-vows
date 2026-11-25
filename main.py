#!/usr/bin/env python3
"""One-line robot wedding vows — make.fun bounty entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt: exactly 116 characters, no trailing newline.
"""

import os

LINE = "I promise to love you through every firmware update, every low battery, and every reboot \u2014 until death do us unplug."

# Bounty gate: the entry must be 1-200 characters with no trailing newline.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check against the bounty gate: read back the bytes we just
    # wrote and fail loudly if the gate is missed.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS, "entry length out of gate"
    assert not data.endswith(b"\n"), "entry must not end with a newline"
    # Strongest check: the bytes on disk must be exactly the vow line,
    # so a silent drift in LINE or in the write path cannot slip through.
    assert text == LINE, "entry text drifted from LINE"


if __name__ == "__main__":
    main()
