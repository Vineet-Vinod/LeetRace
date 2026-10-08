from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(address='1.1.1.1')", "candidate(address='255.100.50.0')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(address='255.255.255.255')")
    while len(cases) < 600:
        a = ".".join(str(rng.randint(0, 255)) for _ in range(4))
        call = f"candidate(address={a!r})"
        cases.add(call)
    return sorted(cases)
