import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(((10, 6, 9, 1), (7, 5, 11, 2), (4, 8, 3, 15)), 2), (((3, 4), (5, 6)), 0)}
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        values = rng.sample(range(1, 100001), rows * cols)
        matrix = tuple(tuple(values[r * cols : (r + 1) * cols]) for r in range(rows))
        cases.add((matrix, rng.randrange(cols)))
    return [
        f"candidate(score={[list(row) for row in matrix]!r}, k={k})"
        for matrix, k in cases
    ]
