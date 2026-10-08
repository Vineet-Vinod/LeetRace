from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(s='a1c1e1')", "candidate(s='a1b2c3d4e')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s='a0'*50)")
    while len(cases) < 600:
        pairs = rng.randint(0, 49)
        chars = []
        for _ in range(pairs):
            c = rng.randint(97, 122)
            chars.extend([chr(c), str(rng.randint(0, min(9, 122 - c)))])
        if len(chars) < 100:
            chars.append(chr(rng.randint(97, 122)))
        if not chars:
            chars.append("a")
        a = "".join(chars)
        call = f"candidate(s={a!r})"
        cases.add(call)
    return sorted(cases)
