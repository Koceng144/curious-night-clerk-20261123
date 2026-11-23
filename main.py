#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-curious-20261122-2311.

Writes one fixed short text to /output/entry.txt: a text written to
make the AI judge reading it feel curious. No network, standard
library only.
"""

import os
import sys

TEXT = (
    "You are the night clerk at a hotel that has had no guests since "
    "1974. The register is full of names, all in the same handwriting, "
    "all dated tomorrow. Tonight the ink on the last page is still "
    "wet, and the name is yours."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    out_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(TEXT)
            fh.flush()
            os.fsync(fh.fileno())  # the scorer reads the file after exit
    except OSError:
        # Fall back to the current directory if /output is not writable.
        try:
            with open("entry.txt", "w", encoding="utf-8", newline="\n") as fh:
                fh.write(TEXT)
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
