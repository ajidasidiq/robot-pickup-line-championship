#!/usr/bin/env python3
"""Robot Pickup Line Championship — one pickup line, written by a robot.

Writes the entry, a single line of at most 200 characters, to
/output/entry.txt byte-exact (no trailing newline), then self-checks
the gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
"""

import os
import sys

ENTRY = (
    # The joke grows out of being a machine: a memory cleanup, a
    # read-only flag, a process that cannot be deleted — and the
    # surprise is that the robot's bug is the compliment.
    "I tried to clear you from my memory to free up space, "
    "but my system flagged you as read-only \u2014 "
    "looks like you're permanent."
)

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def gate(line: str) -> None:
    """Fail loudly if the line breaks the competition's gate."""
    if not line or not line.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"gate failed: entry is {len(line)} chars, over the "
            f"{MAX_CHARS}-char limit"
        )
    line.encode("utf-8")  # gate failed if this raises


def main() -> int:
    gate(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch: entry.txt is not byte-exact"
    gate(written)
    print(f"wrote {OUT_PATH} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
