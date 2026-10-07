import random


def generate(seed: int = 0) -> list[str]:
    """Construct permutation-matrix positives and repeated-row zero-result cases."""
    rng = random.Random(seed)
    positives = {((1, 0, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 0, 1), (1, 0, 0))}
    while len(positives) < 300:
        size = rng.randint(2, 100)
        columns = list(range(size))
        rng.shuffle(columns)
        positives.add(
            tuple(
                tuple(int(column == columns[row]) for column in range(size))
                for row in range(size)
            )
        )

    negatives = set()
    negatives.add(tuple(tuple(1 for _ in range(100)) for _ in range(100)))
    while len(negatives) < 300:
        rows = rng.randint(2, 100)
        columns = rng.randint(2, 100)
        pattern = [rng.randrange(2) for _ in range(columns)]
        if sum(pattern) < 2:
            pattern[rng.randrange(columns)] = 1
            pattern[rng.randrange(columns)] = 1
        if sum(pattern) < 2:
            pattern[(pattern.index(1) + 1) % columns] = 1
        negatives.add(tuple(tuple(pattern) for _ in range(rows)))

    matrices = sorted(positives) + sorted(negatives)
    assert len(matrices) == len(set(matrices)) == 600
    assert all(1 <= len(matrix) <= 100 for matrix in matrices)
    assert all(1 <= len(row) <= 100 for matrix in matrices for row in matrix)
    assert all(set(row) <= {0, 1} for matrix in matrices for row in matrix)

    def has_special(matrix: tuple[tuple[int, ...], ...]) -> bool:
        row_sums = [sum(row) for row in matrix]
        column_sums = [
            sum(matrix[row][column] for row in range(len(matrix)))
            for column in range(len(matrix[0]))
        ]
        return any(
            matrix[row][column] == 1 and row_sums[row] == 1 and column_sums[column] == 1
            for row in range(len(matrix))
            for column in range(len(matrix[0]))
        )

    assert all(has_special(matrix) for matrix in positives)
    assert all(not has_special(matrix) for matrix in negatives)
    return [f"candidate(mat={[list(row) for row in matrix]!r})" for matrix in matrices]
