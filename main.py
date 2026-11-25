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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
