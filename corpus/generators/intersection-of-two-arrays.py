import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((1, 2, 2, 1), (2, 2)),
        ((4, 9, 5), (9, 4, 9, 8, 4)),
    }
    cases.add(((0, 1000) * 500, (1000, 0) * 500))
    while len(cases) < 600:
        first = tuple(rng.randint(0, 1000) for _ in range(rng.randint(1, 1000)))
        second = tuple(rng.randint(0, 1000) for _ in range(rng.randint(1, 1000)))
        cases.add((first, second))
    return [
        f"candidate(nums1={list(first)!r}, nums2={list(second)!r})"
        for first, second in cases
    ]
