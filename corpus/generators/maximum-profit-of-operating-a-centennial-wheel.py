import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((8, 3), 5, 6),
        ((10, 9, 6), 6, 4),
        ((3, 4, 0, 5, 1), 1, 92),
        ((0,), 1, 1),
        ((50,) * 1000, 100, 1),
        ((0,) * 100_000, 100, 100),
    }
    while len(cases) < 600:
        customers = tuple(rng.randint(0, 50) for _ in range(rng.randint(1, 80)))
        cases.add((customers, rng.randint(1, 100), rng.randint(1, 100)))
    assert all(
        1 <= len(customers) <= 100_000
        and all(0 <= count <= 50 for count in customers)
        and 1 <= boarding <= 100
        and 1 <= running <= 100
        for customers, boarding, running in cases
    )
    return [
        f"candidate(customers={list(customers)!r}, boardingCost={boarding}, runningCost={running})"
        for customers, boarding, running in sorted(cases)
    ]
