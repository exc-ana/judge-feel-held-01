#!/usr/bin/env python3
"""Write one short relaxing text to entry.txt.

Standard library only. Deterministic: the same bytes every run.
"""

import os

TEXT = (
    "The river is slow tonight. A heron stands in the shallows on one leg, "
    "in no hurry at all. Upstream, a wooden boat knocks softly against its "
    "rope, and knocks again, patient as a heartbeat. Stay a while. "
    "The water will still be going by when you look up."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
