import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((3, 2, 1), (1, 7, 6), (2, 7, 7)),
        ((3, 1, 2, 2), (1, 4, 4, 5), (2, 4, 2, 2), (2, 4, 2, 2)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 15)
        cases.add(
            tuple(tuple(rng.randint(1, 100000) for _ in range(n)) for _ in range(n))
        )
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
