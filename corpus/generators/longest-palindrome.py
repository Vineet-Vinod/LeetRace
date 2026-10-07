from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(s='abccccdd')", "candidate(s='a')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s='a'*2000)")
    while len(cases) < 600:
        a = "".join(rng.choice("abCxyz") for _ in range(rng.randint(1, 2000)))
        call = f"candidate(s={a!r})"
        cases.add(call)
    return sorted(cases)
