from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(s='5F3Z-2e-9-w', k=4)", "candidate(s='2-5g-3-J', k=2)"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s='a'*100000, k=10000)")
    while len(cases) < 600:
        raw = "".join(rng.choice("abcXYZ0123456789") for _ in range(rng.randint(1, 30)))
        a = "-".join(raw[i : i + rng.randint(1, 3)] for i in range(0, len(raw), 3))
        k = rng.randint(1, 10)
        call = f"candidate(s={a!r}, k={k})"
        cases.add(call)
    return sorted(cases)
