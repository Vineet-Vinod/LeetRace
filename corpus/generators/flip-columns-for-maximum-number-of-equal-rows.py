import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((0, 1), (1, 1)), ((0, 1), (1, 0)), ((0, 0, 0), (0, 0, 1), (1, 1, 0))}
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        cases.add(
            tuple(tuple(rng.randint(0, 1) for _ in range(cols)) for _ in range(rows))
        )
    return [f"candidate(matrix={[list(row) for row in matrix]!r})" for matrix in cases]
