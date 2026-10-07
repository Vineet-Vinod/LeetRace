from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(words=['adc', 'wzy', 'abc'])",
    "candidate(words=['aaa', 'bob', 'ccc', 'ddd'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(words=['a'*100]*99+['b'+'a'*99])")
    while len(cases) < 600:
        n = rng.randint(2, 15)
        base = [rng.randint(0, 25) for _ in range(n)]
        words = ["".join(chr(97 + x) for x in base)]
        for _ in range(rng.randint(2, 8)):
            vals = [rng.randint(0, 25) for _ in range(n)]
            while vals == base:
                vals = [rng.randint(0, 25) for _ in range(n)]
            words.append("".join(chr(97 + x) for x in vals))
        # make exactly one unique signature by using a repeated common string and one distinct string
        common = "".join(chr(97 + rng.randint(0, 25)) for _ in range(n))
        first = chr((ord(common[0]) - 96) % 26 + 97)
        odd = first + common[1:]
        words = [common, common, odd]
        rng.shuffle(words)
        call = f"candidate(words={words!r})"
        cases.add(call)
    return sorted(cases)
