#!/usr/bin/env python3
"""Midnight Fridge Roast entry.

Writes one original roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt as a fallback). Stdlib only, no network.
"""
import os

LINE = (
    "My fridge locks at midnight to protect my health \u2014 "
    "bold talk from a box that hums all night and hides the ice cream."
)


def main() -> None:
    # Pre-write guard: the roast line must be a single line of 1-200 chars.
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"roast line length {len(LINE)} outside 1-200 chars")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("roast line must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # UTF-8 read-back round-trip: what we wrote must read back verbatim.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE + "\n":
            raise ValueError("entry.txt round-trip verification failed")


if __name__ == "__main__":
    main()
