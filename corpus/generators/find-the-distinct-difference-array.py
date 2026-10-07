import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1,), (1, 2, 3, 4, 5), (3, 2, 3, 4, 2)}
    cases.add(tuple(range(1, 51)))
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 50) for _ in range(rng.randint(1, 50))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
