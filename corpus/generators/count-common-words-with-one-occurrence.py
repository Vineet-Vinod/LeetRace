from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(words1=['leetcode', 'is', 'amazing', 'as', 'is'], words2=['amazing', 'leetcode', 'is'])",
    "candidate(words1=['b', 'bb', 'bbb'], words2=['a', 'aa', 'aaa'])",
    "candidate(words1=['a', 'ab'], words2=['a', 'a', 'a', 'ab'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(words1=['a']*1000, words2=['a']*1000)")
    while len(cases) < 600:
        pool = [chr(97 + i) for i in range(rng.randint(1, 10))]
        a = [rng.choice(pool) for _ in range(rng.randint(1, 20))]
        b = [rng.choice(pool) for _ in range(rng.randint(1, 20))]
        call = f"candidate(words1={a!r}, words2={b!r})"
        cases.add(call)
    return sorted(cases)
