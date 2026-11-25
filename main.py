#!/usr/bin/env python3
"""Write the one-line excuse for The Excuse That Almost Works.

The program outputs a single line of plain text: the text a gamer sends
their boss to skip work during GTA 6 launch week. It must read like a
message typed in a hurry, stay within twenty words, and fit the gate of
1 to 140 characters.
"""

import os
import sys

# The excuse itself: a boring, specific, almost-believable council mix-up,
# with one word in it that quietly gives the whole thing away. The last
# clause is the kicker a hurried text needs: no way in, no way out.
EXCUSE = (
    "Council towed my car for resurfacing, it's at the Leonida depot "
    "till Friday and the buses don't stop here."
)


def _die(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def _validate(text):
    if not text.strip():
        _die("entry is blank")
    if "\n" in text or "\r" in text:
        _die("entry must be a single line")
    words = text.split()
    if len(words) > 20:
        _die("entry is %d words, over the 20-word limit" % len(words))
    if not 1 <= len(text) <= 140:
        _die("entry is %d characters, outside the 1-140 gate" % len(text))


def _output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def run():
    text = EXCUSE
    _validate(text)
    path = _output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != text:
        _die("round-trip mismatch")
    _validate(stored)
    print("wrote %d words, %d characters to %s" % (len(text.split()), len(text), path))


if __name__ == "__main__":
    run()
