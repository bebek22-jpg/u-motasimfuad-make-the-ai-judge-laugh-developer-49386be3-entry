#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "Production is down because the fix for production being down is in the deploy that took production down."


def main(output_path: str = "/output/entry.txt") -> None:
    text = ENTRY.strip()
    if len(text) > 199:
        raise ValueError(
            f"ENTRY is {len(text)} characters; the competition requires "
            "a single line under 200 characters"
        )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
