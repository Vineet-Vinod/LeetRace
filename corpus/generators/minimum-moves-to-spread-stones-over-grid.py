import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 1, 0), (1, 1, 1), (1, 2, 1)), ((1, 3, 0), (1, 0, 0), (1, 0, 3))}
    while len(cases) < 600:
        cells = [0] * 9
        for _ in range(9):
            cells[rng.randrange(9)] += 1
        cases.add(tuple(tuple(cells[r * 3 + c] for c in range(3)) for r in range(3)))
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
