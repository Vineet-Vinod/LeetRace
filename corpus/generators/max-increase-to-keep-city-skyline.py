import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((3, 0, 8, 4), (2, 4, 5, 7), (9, 2, 6, 3), (0, 3, 1, 0)),
        ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
    }
    while len(cases) < 600:
        n = rng.randint(2, 20)
        cases.add(tuple(tuple(rng.randint(0, 100) for _ in range(n)) for _ in range(n)))
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
