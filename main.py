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


if __name__ == "__main__":
    main()
