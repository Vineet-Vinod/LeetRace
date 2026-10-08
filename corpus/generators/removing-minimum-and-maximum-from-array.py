import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 10, 7, 5, 4, 1, 8, 6), (0, -4, 19, 1, 8, -2, -3, 5), (101,)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add(tuple(rng.sample(range(-(10**5), 10**5 + 1), n)))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
