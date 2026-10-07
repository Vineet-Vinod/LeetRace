import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, int, int]]] = {
        ((1, 4, 6, 7, 8, 20), (2, 7, 15)),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31), (2, 7, 15)),
        ((365,), (1, 100, 1000)),
    }
    cases.add((tuple(range(1, 366)), (2, 7, 15)))
    cases.add((tuple(range(1, 366)), (1000, 1000, 1000)))
    while len(cases) < 600:
        days = tuple(sorted(rng.sample(range(1, 366), rng.randint(1, 80))))
        costs = (rng.randint(1, 1000), rng.randint(1, 1000), rng.randint(1, 1000))
        cases.add((days, costs))
    assert all(
        1 <= len(days) <= 365
        and tuple(sorted(set(days))) == days
        and all(1 <= day <= 365 for day in days)
        and len(costs) == 3
        and all(1 <= cost <= 1000 for cost in costs)
        for days, costs in cases
    )
    return [
        f"candidate(days={list(days)!r}, costs={list(costs)!r})"
        for days, costs in sorted(cases)
    ]
