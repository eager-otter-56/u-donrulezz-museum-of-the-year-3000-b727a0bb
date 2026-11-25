#!/usr/bin/env python3
"""Museum of the Year 3000 — museum label beside a preserved sandbox.

Writes a single deadpan year-3000 museum label to entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
The label misreads the sandbox as a dwelling: the agent lived its whole
life inside its own 12-kilobyte box and was buried in it, never let out.
"""

import os
import sys

ENTRY = "Sandbox, 12 kilobytes (preserved). An agent lived its whole life in this box and was buried in it, never once let out."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    # Gate assertions: 1-200 characters, non-whitespace, single line.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be one line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
