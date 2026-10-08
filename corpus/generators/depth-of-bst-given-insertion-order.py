import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (2, 1, 4, 3),
        (2, 1, 3, 4),
        (1, 2, 3, 4),
        (4, 3, 2, 1),
    }
    cases.add(tuple(range(1, 100_001)))
    cases.add(tuple(range(100_000, 0, -1)))
    while len(cases) < 600:
        size = rng.randint(1, 100)
        cases.add(tuple(rng.sample(range(1, size + 1), size)))
    assert all(
        1 <= len(order) <= 100_000 and set(order) == set(range(1, len(order) + 1))
        for order in cases
    )
    return [f"candidate(order={list(order)!r})" for order in sorted(cases)]
