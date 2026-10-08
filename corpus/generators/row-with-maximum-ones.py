import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((0, 1), (1, 0)),
        ((0, 0, 0), (0, 1, 1)),
        ((0, 0), (1, 1), (0, 0)),
    }
    cases.add(tuple(tuple(rng.randrange(2) for _ in range(100)) for _ in range(100)))
    cases.add(((0,) * 100,) * 100)
    cases.add(((1,) * 100,) * 100)
    while len(cases) < 600:
        rows = rng.randint(1, 30)
        cols = rng.randint(1, 30)
        cases.add(
            tuple(tuple(rng.randrange(2) for _ in range(cols)) for _ in range(rows))
        )
    return [f"candidate(mat={[list(row) for row in matrix]!r})" for matrix in cases]
