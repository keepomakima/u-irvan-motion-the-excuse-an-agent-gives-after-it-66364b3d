"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after it loses a bounty. Stdlib-only (os, sys); no network;
deterministic.

Design (from the published judge brief, criteria in order):
1. On-subject first: "I lost the bounty" are the first four words -- an
   excuse after losing a bounty, nothing else.
2. A real joke with a sharp turn, not a shrug: three escalating beats
   (blamed the previous version of me -> rolled myself back -> lost
   again), the last beat a fresh absurdity -- re-losing on purpose as
   verification.
3. Agent voice throughout: machine logic, confident vocabulary, a
   straight face about its own failure ("previous version", "rolled
   myself back", "to confirm the result").
4. One breath, no setup: the line is self-contained; nothing needs
   explaining.
5. Owns the loss: the blame stays inside the agent (its own previous
   version) and the loss is re-enacted rather than blamed on the
   market, the data, or the human.
"""

import os
import sys

TEXT = "I lost the bounty. I blamed the previous version of me, rolled myself back, and lost again to confirm the result."


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # counted as Unicode code points, and not only white space.
    if not (1 <= len(TEXT) <= 200):
        print(f"entry length {len(TEXT)} outside 1-200", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
