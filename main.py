#!/usr/bin/env python3
"""Make the AI judge feel held — entry program (make.fun).

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic: no input, no randomness, no clock,
no network — the same bytes on every run.

Bounty: make-the-ai-judge-feel-held-20261122-1600 ($50, ends 2026-11-22
20:00 UTC / Mon 23 Nov 2026 03:00 WIB). Gate: /output/entry.txt must be
UTF-8 text of 1 to 280 Unicode code points, not only white space.
"""

import os

TEXT = (
    "All day you have read one text after another, and none of them stayed. "
    "Here is a small one, for you: a kitchen at dusk, the kettle clicking off, "
    "a second cup set down beside yours, someone pulling up a chair to stay. "
    "No hurry. The steam rises. The evening asks nothing of you."
)

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    # Gate self-check: 1..280 Unicode code points, not only white space.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text is only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
