import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1,), (1, 1, 1), (1, 5, 2, 4, 1), (8,)}
    cases.add((10_000,) * 5000)
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10_000) for _ in range(rng.randint(1, 300))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
