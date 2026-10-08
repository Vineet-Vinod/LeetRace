import random


def _lucky_numbers(matrix: list[list[int]]) -> list[int]:
    column_maxima = [max(column) for column in zip(*matrix)]
    return sorted(min(row) for row in matrix if min(row) in column_maxima)


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    nonempty: set[str] = set()
    empty: set[str] = set()
    examples = [
        [[3, 7, 8], [9, 11, 13], [15, 16, 17]],
        [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]],
        [[7, 8], [1, 2]],
    ]
    nonempty.update(f"candidate(matrix={matrix!r})" for matrix in examples)

    while len(nonempty) < 300:
        rows, columns = rng.randint(2, 20), rng.randint(2, 20)
        row, column = rng.randrange(rows), rng.randrange(columns)
        matrix = [[0] * columns for _ in range(rows)]
        matrix[row][column] = 50000
        used = {50000}
        row_values = rng.sample(range(50001, 100001), columns - 1)
        column_values = rng.sample(range(1, 50000), rows - 1)
        for index, value in enumerate(row_values):
            target_column = index if index < column else index + 1
            matrix[row][target_column] = value
            used.add(value)
        for index, value in enumerate(column_values):
            target_row = index if index < row else index + 1
            matrix[target_row][column] = value
            used.add(value)
        remaining = [
            (r, c) for r in range(rows) for c in range(columns) if matrix[r][c] == 0
        ]
        values = rng.sample(
            [value for value in range(1, 100001) if value not in used], len(remaining)
        )
        for (r, c), value in zip(remaining, values):
            matrix[r][c] = value
        assert _lucky_numbers(matrix)
        assert len({value for values in matrix for value in values}) == rows * columns
        nonempty.add(f"candidate(matrix={matrix!r})")

    while len(empty) < 300:
        rows, columns = rng.randint(2, 20), rng.randint(2, 20)
        values = rng.sample(range(1, 100001), rows * columns)
        matrix = [
            values[index * columns : (index + 1) * columns] for index in range(rows)
        ]
        if _lucky_numbers(matrix):
            continue
        assert len({value for values in matrix for value in values}) == rows * columns
        empty.add(f"candidate(matrix={matrix!r})")

    return sorted(nonempty | empty)
