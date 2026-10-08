from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(s='XXX')", "candidate(s='XXOX')", "candidate(s='OOOO')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s='O'*1000)")
    cases.add("candidate(s='OOO')")
    while len(cases) < 600:
        a = "".join(rng.choice("XO") for _ in range(rng.randint(3, 1000)))
        call = f"candidate(s={a!r})"
        cases.add(call)
    assert all(3 <= len(eval(call[len("candidate(s=") : -1])) <= 1000 for call in cases)
    assert all(
        set(eval(call[len("candidate(s=") : -1])) <= {"X", "O"} for call in cases
    )
    return sorted(cases)
