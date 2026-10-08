import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((5, 4, 5), (1, 2, 6), (7, 4, 6)),
        ((2, 2, 1, 2, 2, 2), (1, 2, 2, 2, 1, 2)),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        cases.add(
            tuple(
                tuple(rng.randint(0, 10**9) for _ in range(cols)) for _ in range(rows)
            )
        )
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
