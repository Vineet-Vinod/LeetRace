import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((0, 1), (1, 0)),
        ((0, 0, 0), (1, 1, 0), (1, 1, 0)),
        ((1, 0, 0), (1, 1, 0), (1, 1, 0)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 20)
        grid = [[rng.randint(0, 1) for _ in range(n)] for _ in range(n)]
        cases.add(tuple(tuple(row) for row in grid))
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
