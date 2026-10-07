from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums1=[1, 2, 3], nums2=[2, 4])",
    "candidate(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums1=list(range(1,100001)), nums2=list(range(1,100001)))")
    while len(cases) < 600:
        a = sorted(rng.sample(range(1, 1001), rng.randint(1, 30)))
        b = sorted(rng.sample(range(1, 1001), rng.randint(1, 30)))
        call = f"candidate(nums1={a!r}, nums2={b!r})"
        cases.add(call)
    return sorted(cases)
