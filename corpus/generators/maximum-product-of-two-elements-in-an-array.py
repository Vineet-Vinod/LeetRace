import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(3, 4, 5, 2), (1, 5, 4, 5), (3, 7)}
    cases.add((1000, 1000) + (1,) * 498)
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 1000) for _ in range(rng.randint(2, 500))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
