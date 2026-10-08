import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 3, 1, 7), (1, 3, 2, 4), 1), ((1, 2, 3), (10,), 5)}
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 10000) for _ in range(rng.randint(1, 100)))
        queries = tuple(rng.randint(1, 100000) for _ in range(rng.randint(1, 50)))
        cases.add((nums, queries, rng.randint(1, 10000)))
    return [
        f"candidate(nums={list(nums)!r}, queries={list(queries)!r}, x={x})"
        for nums, queries, x in cases
    ]
