import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(5, 3, 2, 4), (1, 5, 0, 10, 14), (3, 100, 20)}
    while len(cases) < 600:
        cases.add(
            tuple(rng.randint(-(10**9), 10**9) for _ in range(rng.randint(1, 100)))
        )
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
