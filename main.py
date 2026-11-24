#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only things such a person would already know:
a town square, a letter, a board. No word in the sentence was coined
after the traveler's time.

The program writes the sentence to /output/entry.txt by default, or to
the path in the OUTPUT_PATH environment variable for local testing.
"""

import os
from pathlib import Path

ENTRY = (
    "It is a town square where anyone may pin a letter to a board and "
    "have it read in a thousand towns before supper, and answer any "
    "letter pinned there."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT))

    # The gate: 1-200 characters, not only whitespace, no newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")

    # Round-trip check: what was written must read back byte-identical
    # and still pass the gate, so a run can never silently corrupt it.
    written = output_path.read_text(encoding="utf-8")
    assert written == ENTRY, "round-trip mismatch"
    assert 1 <= len(written) <= 200, f"written entry is {len(written)} characters"
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
