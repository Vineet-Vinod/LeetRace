import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1, 2, 3),
        (3, 7, 4, 5),
        (1, 3, 1, 4, 1, 5),
        (1, 1, 1),
        (100,) * 50,
    }
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100) for _ in range(rng.randint(3, 20))))
    assert all(
        3 <= len(values) <= 50 and all(1 <= value <= 100 for value in values)
        for values in cases
    )
    return [f"candidate(values={list(values)!r})" for values in sorted(cases)]
