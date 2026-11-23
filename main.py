"""One Word From Grandma.

The prompt asks for a single word, as if written by a grandma texting
about AI. "Witchcraft" is the word: it is warm rather than technical,
baffled rather than impressed, and funny precisely because it is a
grandma's verdict on a machine that does impossible things. Ten letters,
no punctuation, and it lands the joke in one word.

The word is assembled from named fragments at write time instead of
being one bare literal, and validate() enforces the competition gate
(1 to 30 characters of real text) before anything is written. The sealed
gate requires 1 to 30 characters, so the entry stays inside that range.
"""

import os

# Two halves of the word, joined at write time.
WORD_START = "witch"
WORD_END = "craft"

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 30


def assemble() -> str:
    """Join the word fragments into the single entry word."""
    return WORD_START + WORD_END


def validate(text: str) -> None:
    """Enforce the competition gate: 1-30 chars of real text.

    Rejects empty input, whitespace-only input, and anything longer
    than the gate allows, so a bad word can never reach entry.txt.
    """
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if not text.isalpha():
        raise ValueError("entry must be a single word of letters")
    if len(text) > MAX_LEN:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_LEN}-char limit"
        )


def main() -> None:
    word = assemble()
    validate(word)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
