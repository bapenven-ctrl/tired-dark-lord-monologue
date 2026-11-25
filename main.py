#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue (102 words, 552 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no clock. UTF-8, no BOM,
no trailing newline. Gate: 1-600 UTF-8 characters.
"""

import os

TEXT = (
    "Tuesday's skull goes on the third shelf, left side, labeled in ink that does not fade. "
    "Wednesday's skull goes beside it, slightly smaller, slightly smug. "
    "I know every skull by name, by weight, by the joke it told on its last day. "
    "The first label reads: 'Borin the Bold \u2014 came on a Tuesday, asked what the labels mean.' "
    "The second reads the same, only the name is different. "
    "Nine hundred and ninety-nine skulls, each remembered, and one empty space at the end. "
    "Come closer. Read the first one. "
    "Then tell me your name, hero \u2014 slowly, so I spell it right."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
