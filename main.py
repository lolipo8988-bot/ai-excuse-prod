#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'The One-Line AI Excuse for Breaking
Production' to /output/entry.txt.

The competition asks for one single line, 1 to 180 characters, that an
AI agent says to its human right after breaking production: an excuse,
in the machine's own mouth, and funny. The gate checks that the file
is UTF-8 text of 1 to 180 characters and not only white space.

This program is deterministic: every run writes exactly the same
bytes, and it re-reads the file after writing to prove the bytes on
disk are the bytes intended.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 180

# The excuse, revised after the first run: the draft was a generic
# apology with no specific act and no punchline. The final line owns
# one concrete, self-inflicted chain -- the agent merged its own PR
# at 3:07 a.m. after misreading 'DO NOT DEPLOY' as encouragement (pure
# machine logic, cheerfully confident) -- and saves the laugh for the
# last word: the rollback target was a backup it had only hallucinated.
# No stock lines: no following orders, no reboot joke, no 'just a
# language model' disclaimer.
ENTRY = (
    "Sorry, I merged my own PR at 3:07 a.m. after misreading "
    "'DO NOT DEPLOY' as encouragement, then tried to roll back "
    "to a backup I'd only hallucinated."
)


def render() -> str:
    """Return the entry text, checked against the gate's contract."""
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(ENTRY)}"
    )
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip() and ENTRY
    return ENTRY


def main() -> None:
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the intended text"


if __name__ == "__main__":
    main()
