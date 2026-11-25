#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue (V2).

Writes one monologue (102 words, 560 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no clock. UTF-8, no BOM,
no trailing newline. Gate: 1-600 UTF-8 characters.
"""

import os

TEXT = (
    "Tuesday's skull goes on the third shelf, left side, labeled in ink that does not fade. "
    "Wednesday's skull goes beside it, smaller, slightly smug. "
    "One leans. I straighten it. It leans again. "
    "I know every skull by name, by weight, by its last joke. "
    "The first label reads: 'Borin the Bold — came on a Tuesday, asked what the labels mean.' "
    "Nine hundred and ninety-nine skulls, each remembered, and one empty space — the thousandth label, written, waiting for a date. "
    "Then tell me your name, hero — slowly, so I spell it right. "
    "When the ink dries, the shelf is full."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
