import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((1, 2, 2, 1, 2, 3, 1), ((1, 2), (3, 3), (4, 2))),
        ((1, 4, 2, 3), ((0, 1),)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 80)
        nums = tuple(rng.randint(1, 100000) for _ in range(n))
        m = rng.randint(1, n)
        queries = tuple((rng.randrange(n), rng.randint(0, n - 1)) for _ in range(m))
        cases.add((nums, queries))
    return [
        f"candidate(nums={list(nums)!r}, queries={[list(q) for q in queries]!r})"
        for nums, queries in cases
    ]
