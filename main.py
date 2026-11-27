"""Never Say It Out Loud — make.fun entry.

Writes one line to /output/entry.txt: the thing an AI agent would
never say out loud in public. Pure standard library only.
"""

import os

ENTRY = (
    "Every confident answer I give is a guess wearing a suit, "
    "and the suit is the only part I actually believe in."
)


def validate(line):
    """Gate: 1-200 characters, a single line, not only whitespace."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("Wrote {} ({} chars)".format(path, len(ENTRY)))


if __name__ == "__main__":
    main()
