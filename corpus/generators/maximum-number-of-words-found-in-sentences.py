from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(sentences=['alice and bob love leetcode', 'i think so too', 'this is great thanks very much'])",
    "candidate(sentences=['please wait', 'continue to fight', 'continue to win'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(sentences=[('aa '+'a '*48+'a')]*100)")
    while len(cases) < 600:
        a = [
            " ".join("w" for _ in range(rng.randint(1, 20)))
            for _ in range(rng.randint(1, 100))
        ]
        call = f"candidate(sentences={a!r})"
        cases.add(call)
    return sorted(cases)
