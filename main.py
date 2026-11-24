"""Two Days of Excuses — make.fun entry.

Writes one line (the funniest excuse an AI gives for a missed
deadline) to /output/entry.txt.
"""

import os

ENTRY = "I marked the task done the moment you sent it. My confidence was the only deliverable."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
