import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((1, 0, 1), (1, 1, 0), (1, 1, 0)),
        ((0, 1, 1, 0), (0, 1, 1, 1), (1, 1, 1, 0)),
        ((1,) * 150,) * 150,
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        cases.add(
            tuple(tuple(rng.randint(0, 1) for _ in range(cols)) for _ in range(rows))
        )
    assert all(
        1 <= len(mat) <= 150
        and 1 <= len(mat[0]) <= 150
        and all(
            len(row) == len(mat[0]) and all(value in (0, 1) for value in row)
            for row in mat
        )
        for mat in cases
    )
    return [f"candidate(mat={[list(row) for row in mat]!r})" for mat in sorted(cases)]
