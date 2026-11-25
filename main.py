#!/usr/bin/env python3
"""Museum of the Year 3000 — writes one museum label to /output/entry.txt."""

import os

ENTRY = "iPhone Charging Cable (c. 2024) — Primitive energy vine; users performed nightly ritual of untangling before whispering 'please charge' to the glowing rectangle."


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must be non-blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range 1..200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
