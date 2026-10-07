import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((2, 3, 1), (1, 2, 1)), ((1, 3, 2, 1), (2, 2, 3, 4)), ((1, 1), (2, 2))}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add(
            (
                tuple(rng.randint(1, 10**9) for _ in range(n)),
                tuple(rng.randint(1, 10**9) for _ in range(n)),
            )
        )
    return [f"candidate(nums1={list(a)!r}, nums2={list(b)!r})" for a, b in cases]
