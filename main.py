#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - entry program.

Writes one debugging haiku (three lines, 5-7-5 syllables, plain text)
to /output/entry.txt, exactly as the competition gate expects:
UTF-8 text of 1 to 200 characters, not only white space.
"""
import os

LINES = [
    "the error points up",
    "the trace runs through others' code",
    "the last frame is mine",
]


def main():
    text = "\n".join(LINES)
    # Kit gate asserts: 1 to 200 characters, not only white space,
    # and the haiku shape of exactly three lines.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry is only white space"
    assert len(LINES) == 3, "a haiku has three lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"GATE OK: {len(text)} characters, {len(LINES)} lines")


if __name__ == "__main__":
    main()
