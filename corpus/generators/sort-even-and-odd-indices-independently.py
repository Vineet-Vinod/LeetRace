import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(4, 1, 2, 3), (2, 1)}
    cases.add((1,) * 50 + (100,) * 50)
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
