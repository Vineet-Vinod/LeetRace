import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((4, 1, 3), (5, 7)),
        ((3, 5, 2, 6), (3, 1, 7)),
    }
    digits = range(1, 10)
    cases.add((tuple(range(1, 10)), tuple(range(1, 10))))
    while len(cases) < 600:
        first = tuple(sorted(rng.sample(digits, rng.randint(1, 9))))
        second = tuple(sorted(rng.sample(digits, rng.randint(1, 9))))
        cases.add((first, second))
    return [
        f"candidate(nums1={list(first)!r}, nums2={list(second)!r})"
        for first, second in cases
    ]
