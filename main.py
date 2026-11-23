#!/usr/bin/env python3
"""One Word From Grandma (u-0xkianno-one-word-from-grandma-f04bed16) — make.fun program/v1 entry.

Writes one line to /output/entry.txt (gate: 1 to 30 characters).
Deterministic, stdlib only, no network, no randomness, no time.
Author: stellarlumens29 (make.fun handle stellar-lumens).
"""

import os

ENTRY = 'whatchamacallit'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 30, f"entry length {len(text)} out of range 1-30"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be blank"
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            continue


if __name__ == "__main__":
    main()
