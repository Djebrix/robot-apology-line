"""The Robot Apology — a two-line apology from a household robot.

Writes exactly two lines to $ENTRY_OUTPUT_DIR/entry.txt:
line 1 names one concrete mistake, line 2 names the lesson it
taught and the specific thing the robot will do differently.
Deterministic, stdlib only, no network.
"""

import os

ENTRY_TEXT = (
    "I watered the plastic ficus every morning for six weeks while the real fern next to it died of thirst.\n"
    "I learned a schedule is not the same as care, so I will tap each leaf before I water it.\n"
)


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
