import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 3, 2, 4, 1), 7),
        ((10, 6, 8, 7, 7, 8), 5),
        ((1, 6, 3, 1, 2, 5), 20),
        ((1,), 1),
        ((100_000,) * 100_000, 10**8),
    }
    while len(cases) < 600:
        costs = tuple(rng.randint(1, 100_000) for _ in range(rng.randint(1, 80)))
        cases.add((costs, rng.randint(1, 10**8)))
    assert all(
        1 <= len(costs) <= 100_000
        and 1 <= coins <= 10**8
        and all(1 <= cost <= 100_000 for cost in costs)
        for costs, coins in cases
    )
    return [
        f"candidate(costs={list(costs)!r}, coins={coins})"
        for costs, coins in sorted(cases)
    ]
