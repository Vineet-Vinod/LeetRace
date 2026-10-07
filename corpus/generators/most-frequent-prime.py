def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    examples = [
        [[1, 1], [9, 9], [1, 1]],
        [[7]],
        [[9, 7, 8], [4, 6, 5], [2, 8, 6]],
    ]
    matrices = {tuple(tuple(row) for row in mat) for mat in examples}
    matrices.add(tuple(tuple(9 for _ in range(6)) for _ in range(6)))
    matrices.add(tuple(tuple(1 for _ in range(6)) for _ in range(6)))
    while len(matrices) < 600:
        rows, columns = rng.randint(1, 6), rng.randint(1, 6)
        matrix = tuple(
            tuple(rng.randint(1, 9) for _ in range(columns)) for _ in range(rows)
        )
        matrices.add(matrix)

    calls = []
    for matrix in sorted(matrices):
        rows = [list(row) for row in matrix]
        assert 1 <= len(rows) <= 6
        assert all(1 <= len(row) <= 6 for row in rows)
        assert len({len(row) for row in rows}) == 1
        assert all(1 <= digit <= 9 for row in rows for digit in row)
        calls.append(f"candidate(mat={rows!r})")
    return calls
