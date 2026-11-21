"""make.fun bounty: make-the-ai-judge-feel-awe-20261121-1600.

Reads the short text shipped in entry.txt, beside this script, and writes it
byte for byte to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Standard
library only, no network, no arguments, no fallback text.
"""

import os
from pathlib import Path

BOUNTY = "make-the-ai-judge-feel-awe-20261121-1600"
DEFAULT_OUTPUT_DIR = "/output"


def entry_path() -> Path:
    """The hand-in text shipped in the repository, beside this script."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """The file the grader reads: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)) / "entry.txt"


def main() -> None:
    """Copy entry.txt to the output directory, adding and changing nothing."""
    source = entry_path()
    if not source.is_file():
        raise FileNotFoundError(f"{BOUNTY}: missing {source}")

    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)

    # Bytes, not text: the text reaches the grader exactly as it was authored.
    target.write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()
