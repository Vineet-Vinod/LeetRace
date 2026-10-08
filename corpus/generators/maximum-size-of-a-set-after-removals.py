import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((1, 2, 1, 2), (1, 1, 1, 1)),
        ((1, 2, 3, 4, 5, 6), (2, 3, 2, 3, 2, 3)),
        ((1, 1, 2, 2, 3, 3), (4, 4, 5, 5, 6, 6)),
    }
    while len(cases) < 600:
        n = 2 * rng.randint(1, 40)
        cases.add(
            (
                tuple(rng.randint(1, 100) for _ in range(n)),
                tuple(rng.randint(1, 100) for _ in range(n)),
            )
        )
    return [f"candidate(nums1={list(a)!r}, nums2={list(b)!r})" for a, b in cases]
