from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(emails=['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com'])",
    "candidate(emails=['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(emails=['a@b.com']*100)")
    while len(cases) < 600:
        a = []
        for _ in range(rng.randint(1, 100)):
            local = "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz")
                for _ in range(rng.randint(1, 10))
            )
            if rng.random() < 0.5:
                local += "+" + "".join(rng.choice("abc") for _ in range(3))
            if len(local) > 1 and rng.random() < 0.5:
                local = local[0] + "." + local[1:]
            domain = (
                "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 8))) + ".com"
            )
            a.append(local + "@" + domain)
        call = f"candidate(emails={a!r})"
        cases.add(call)
    return sorted(cases)
