from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(s='foobar', letter='o')", "candidate(s='jjjj', letter='k')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s='a'*100, letter='a')")
    while len(cases) < 600:
        a = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 100))
        )
        c = rng.choice("abcdefghijklmnopqrstuvwxyz")
        call = f"candidate(s={a!r}, letter={c!r})"
        cases.add(call)
    return sorted(cases)
