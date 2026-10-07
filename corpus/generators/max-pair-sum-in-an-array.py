import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (112, 131, 411),
        (2536, 1613, 3366, 162),
        (51, 71, 17, 24, 42),
    }
    cases.add((10_000, 9000) + (1,) * 98)
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10_000) for _ in range(rng.randint(2, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
