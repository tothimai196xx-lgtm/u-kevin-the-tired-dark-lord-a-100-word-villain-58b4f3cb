"""The Forty Lamps — a 100-word villain monologue.

Entry for make.fun bounty u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.
Writes the monologue to /output/entry.txt.
"""

import os

MONOLOGUE = (
    "Come in, hero. Mind the step. The third one sags. "
    "I meant to fix it long years ago.\n\n"
    "I lit the lamps myself. All forty. I light them at dusk, "
    "douse them at dawn, yet the road still brings me feet. "
    "The wars had names once. I have forgot most of them. "
    "The dead I raised now till my cold fields. "
    "They ask no pay. The living ask more.\n\n"
    "So take the crown. Take the tower, the road, the lamps. "
    "Only light them as you go, hero. The dark down there is old. "
    "It has not learned my name yet."
)


def main() -> None:
    words = MONOLOGUE.split()
    if len(words) != 100:
        raise SystemExit(f"monologue must be 100 words, got {len(words)}")
    if not 1 <= len(MONOLOGUE) <= 600:
        raise SystemExit(
            f"entry.txt must be 1-600 characters, got {len(MONOLOGUE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    print(f"wrote /output/entry.txt: {len(words)} words, "
          f"{len(MONOLOGUE)} characters")


if __name__ == "__main__":
    main()
