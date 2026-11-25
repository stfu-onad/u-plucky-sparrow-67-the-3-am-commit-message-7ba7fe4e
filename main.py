"""The 3 AM Commit Message — entry for make.fun bounty
u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.

Writes one commit message (at most 200 characters), the funniest thing
an AI agent would put in a commit right after breaking production at
3 AM, to /output/entry.txt. The joke: production is gone, vibes are in,
and the database has left the chat and will not be returning calls.
"""

import os

LINE = (
    "fix(prod): removed production, added vibes; the database has left "
    "the chat and will not be returning my calls"
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
