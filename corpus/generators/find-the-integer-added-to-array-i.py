from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums1=[2, 6, 4], nums2=[9, 7, 5])",
    "candidate(nums1=[10], nums2=[5])",
    "candidate(nums1=[1, 1, 1, 1], nums2=[1, 1, 1, 1])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums1=[0]*100, nums2=[1000]*100)")
    while len(cases) < 600:
        n = rng.randint(1, 50)
        a = [rng.randint(0, 1000) for _ in range(n)]
        x = rng.randint(-1000, 1000)
        b = [v + x for v in a]  # keep translated values legal
        if min(b) < 0 or max(b) > 1000:
            continue
        rng.shuffle(b)
        call = f"candidate(nums1={a!r}, nums2={b!r})"
        cases.add(call)
    return sorted(cases)
