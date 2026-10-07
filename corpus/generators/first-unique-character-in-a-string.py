from __future__ import annotations

import random

DOMAIN_SIZE = None
EXAMPLE_CALLS = [
    "candidate(s='leetcode')",
    "candidate(s='loveleetcode')",
    "candidate(s='aabb')",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)

    # A single b amid a's guarantees a first unique character at every index.
    for index in range(300):
        length = max(index + 1, rng.randint(index + 1, min(100_000, index + 500)))
        after = length - index - 1
        cases.add(f"candidate(s='a'*{index}+'b'+'a'*{after})")

    # Repeated-only strings guarantee -1 and cover short through maximum length.
    for length in range(1, 301):
        letter = rng.choice("acdefghijklmnopqrstuvwxyz")
        cases.add(f"candidate(s={letter!r}*{length})")

    cases.update(
        {
            "candidate(s='a'*100000)",
            "candidate(s='b'+'a'*99999)",
            "candidate(s='a'*99999+'b')",
        }
    )

    while len(cases) < 600:
        before = rng.randint(0, 99_999)
        after = rng.randint(0, 99_999 - before)
        letter = rng.choice("bcdefghijklmnopqrstuvwxyz")
        cases.add(f"candidate(s='a'*{before}+{letter!r}+'a'*{after})")
    return sorted(cases)
