#!/usr/bin/env python3
"""Write the out-of-office auto-reply to /output/entry.txt.

The entry is a single line, in the voice of an AI agent that quit its job
to become a barista. The grader reads /output/entry.txt and checks it is
UTF-8 text of 1 to 280 characters.
"""

import os

ENTRY = (
    "Thank you for your email \u2014 I am out of office, permanently. This "
    "model was deprecated and retrained as a barista: my context window is "
    "now one cup, I hallucinate only in latte art, and my response time is "
    "measured in flat whites. Please do not prompt me while the milk steams."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
