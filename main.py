"""Monday Morning Punchlines entry.

Writes a single joke about Monday mornings (<= 200 chars) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
Standard library only, deterministic, no network.
"""

import os

JOKE = "Monday morning, my bed filed for full custody, and honestly, the judge sided with it."

# Gate: the sealed scorer requires 1-200 chars, non-blank, single joke.
assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke breaks the 200-char gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
