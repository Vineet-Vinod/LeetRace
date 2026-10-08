from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(licensePlate='1s3 PSt', words=['step', 'steps', 'stripe', 'stepple'])",
    "candidate(licensePlate='1s3 456', words=['looks', 'pest', 'stew', 'show'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(licensePlate='1s3 PSt', words=['a'*15]*999+['steps'])")
    while len(cases) < 600:
        required = "".join(rng.choice("abcxyz") for _ in range(rng.randint(0, 5)))
        words = [
            "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz")
                for _ in range(rng.randint(1, 15))
            )
            for _ in range(10)
        ]
        words.append(required + "zz")
        plate = required.upper() + (" 123"[: max(0, 7 - len(required))])
        call = f"candidate(licensePlate={plate!r}, words={words!r})"
        cases.add(call)
    return sorted(cases)
