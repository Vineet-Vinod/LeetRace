import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(7,), (-1, 5, 2), (1, 2, 3), (3, 2, 1)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add(tuple(rng.sample(range(-(10**5), 10**5 + 1), n)))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
