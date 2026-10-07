import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 1, 0, 1), (0, 1, 1, 0)), ((0, 1), (1, 1)), ((0,), (1,))}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add(
            (
                tuple(rng.randint(0, 1) for _ in range(n)),
                tuple(rng.randint(0, 1) for _ in range(n)),
            )
        )
    return [f"candidate(nums1={list(a)!r}, nums2={list(b)!r})" for a, b in cases]
