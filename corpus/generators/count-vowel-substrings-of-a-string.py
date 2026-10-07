from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(word='aeiouu')",
    "candidate(word='unicornarihan')",
    "candidate(word='cuaieuouac')",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(word='aeiou'*20)")
    while len(cases) < 600:
        a = "".join(rng.choice("aeioubcdf") for _ in range(rng.randint(1, 100)))
        call = f"candidate(word={a!r})"
        cases.add(call)
    return sorted(cases)
