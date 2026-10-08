import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19), (2, 1, 4, 3, 9, 6)),
        ((28, 6, 22, 8, 44, 17), (22, 28, 8, 6)),
    }
    cases.add((tuple(range(1, 1000)) + (1000,), tuple(range(1, 1000)) + (1000,)))
    cases.add(((0,) * 999 + (1000,), (1000, 0)))
    while len(cases) < 600:
        arr1 = [rng.randint(0, 1000) for _ in range(rng.randint(1, 200))]
        unique = sorted(set(arr1))
        arr2 = tuple(rng.sample(unique, rng.randint(1, len(unique))))
        cases.add((tuple(arr1), arr2))
    return [
        f"candidate(arr1={list(first)!r}, arr2={list(second)!r})"
        for first, second in cases
    ]
