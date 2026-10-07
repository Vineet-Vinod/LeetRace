import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, ...], ...], int]] = {
        (((1, 2, 3), (4, 5, 6), (7, 8, 9)), 1),
        (((1, 2, 3), (4, 5, 6), (7, 8, 9)), 2),
        (((100,),), 100),
        (tuple(tuple(1 for _ in range(100)) for _ in range(100)), 100),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 18), rng.randint(1, 18)
        mat = tuple(
            tuple(rng.randint(1, 100) for _ in range(cols)) for _ in range(rows)
        )
        cases.add((mat, rng.randint(1, 100)))
    assert all(
        1 <= len(mat) <= 100
        and 1 <= len(mat[0]) <= 100
        and all(
            len(row) == len(mat[0]) and all(1 <= value <= 100 for value in row)
            for row in mat
        )
        and 1 <= k <= 100
        for mat, k in cases
    )
    return [
        f"candidate(mat={[list(row) for row in mat]!r}, k={k})"
        for mat, k in sorted(cases)
    ]
