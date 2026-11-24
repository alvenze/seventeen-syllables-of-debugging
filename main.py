#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - entry program.

Writes one debugging haiku (three lines, 5-7-5 syllables, plain text)
to /output/entry.txt, exactly as the competition gate expects:
UTF-8 text of 1 to 200 characters, not only white space.
"""
import os
import re

LINES = [
    "the error points up",
    "the trace runs through others' code",
    "the last frame is mine",
]
EXPECTED_SYLLABLES = [5, 7, 5]


def count_syllables(word):
    """Vowel-group syllable count for this entry's own fixed words.

    The counts were verified offline against the CMU Pronouncing
    Dictionary; this small counter reproduces them deterministically
    so the program can check its own shape in the sandbox.
    """
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and groups > 1:
        groups -= 1  # silent final e
    return max(groups, 1)


def check_gate(text):
    """The kit's gate, checked by the entry itself before writing."""
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry is only white space"
    lines = text.split("\n")
    assert len(lines) == 3, "a haiku has three lines"
    counts = [sum(count_syllables(w) for w in line.split())
              for line in lines]
    assert counts == EXPECTED_SYLLABLES, f"syllables are {counts}"
    return counts


def main():
    text = "\n".join(LINES)
    counts = check_gate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Post-write self-check: what landed on disk is what was gated.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry differs from the gated text"
    check_gate(written)
    print(f"GATE OK: {len(text)} characters, syllables {counts}")


if __name__ == "__main__":
    main()
