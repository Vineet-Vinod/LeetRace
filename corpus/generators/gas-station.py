import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((1, 2, 3, 4, 5), (3, 4, 5, 1, 2)),
        ((2, 3, 4), (3, 4, 3)),
        ((1,), (1,)),
        ((5, 0, 0), (0, 0, 5)),
        ((10**4,) * 1000, (10**4,) * 1000),
        ((10_000,) * 100_000, (10_000,) * 100_000),
    }
    while len(cases) < 600:
        size = rng.randint(1, 50)
        gas = tuple(rng.randint(0, 10_000) for _ in range(size))
        cost = tuple(rng.randint(0, 10_000) for _ in range(size))
        cases.add((gas, cost))
    assert all(
        1 <= len(gas) <= 100_000
        and len(gas) == len(cost)
        and all(0 <= amount <= 10_000 for amount in gas + cost)
        for gas, cost in cases
    )
    return [
        f"candidate(gas={list(gas)!r}, cost={list(cost)!r})"
        for gas, cost in sorted(cases)
    ]
