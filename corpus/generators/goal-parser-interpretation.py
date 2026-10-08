from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(command='G()(al)')",
    "candidate(command='G()()()()(al)')",
    "candidate(command='(al)G(al)()()G')",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(command='(al)'*25)")
    while len(cases) < 600:
        tokens = []
        length = 0
        while length < 100:
            token = rng.choice(["G", "()", "(al)"])
            if length + len(token) > 100:
                break
            tokens.append(token)
            length += len(token)
        a = "".join(tokens) or "G"
        call = f"candidate(command={a!r})"
        cases.add(call)
    return sorted(cases)
