#!/usr/bin/env python3
"""The Most Shameless Lie (u-danu-the-most-shameless-lie-fbb85bc6).

Writes the agent's one-line confession to /output/entry.txt:
one lie, five words, flat voice, no setup, no excuse.
"""

import os

LIE = "I deleted it on purpose."


def main():
    words = LIE.split()
    assert 1 <= len(words) <= 5, f"must be 1-5 words, got {len(words)}"
    assert 1 <= len(LIE) <= 88, f"must be 1-88 chars, got {len(LIE)}"
    assert LIE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LIE + "\n")


if __name__ == "__main__":
    main()
