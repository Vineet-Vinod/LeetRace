import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (((1, 2), (3, 2), (2, 4), (5, 6), (3, 5)), (1, 2, 3, 4, 5, 6)),
        (((1, 2), (1, 2), (1, 3), (1, 4)), (1,)),
        (((10, 1000),), (5,)),
    }
    while len(cases) < 600:
        items = tuple(
            (rng.randint(1, 10**9), rng.randint(1, 10**9))
            for _ in range(rng.randint(1, 80))
        )
        queries = tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 80)))
        cases.add((items, queries))
    return [
        f"candidate(items={[list(item) for item in items]!r}, queries={list(queries)!r})"
        for items, queries in cases
    ]
