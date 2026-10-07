import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, ...], ...], int]] = {
        (((1, 5, 9), (10, 11, 13), (12, 13, 15)), 8),
        (((-5,),), 1),
    }
    for size in range(1, 301):
        if size in (1, 300):
            value = 1 if size == 1 else 0
            mat = tuple(
                tuple(value + row * size + col for col in range(size))
                for row in range(size)
            )
            cases.add((mat, size * size // 2 + 1))
    while len(cases) < 600:
        size = rng.randint(1, 20)
        mat = []
        for row in range(size):
            current = []
            for col in range(size):
                lower = max(
                    mat[row - 1][col] if row else -(10**9),
                    current[col - 1] if col else -(10**9),
                )
                current.append(lower + rng.randint(0, 5))
            mat.append(current)
        matrix = tuple(tuple(values) for values in mat)
        cases.add((matrix, rng.randint(1, size * size)))
    assert all(
        1 <= len(matrix) <= 300
        and all(len(row) == len(matrix) for row in matrix)
        and all(-(10**9) <= value <= 10**9 for row in matrix for value in row)
        and 1 <= k <= len(matrix) ** 2
        and all(
            matrix[row][col] <= matrix[row][col + 1]
            for row in range(len(matrix))
            for col in range(len(matrix) - 1)
        )
        and all(
            matrix[row][col] <= matrix[row + 1][col]
            for row in range(len(matrix) - 1)
            for col in range(len(matrix))
        )
        for matrix, k in cases
    )
    return [
        f"candidate(matrix={[list(row) for row in matrix]!r}, k={k})"
        for matrix, k in sorted(cases)
    ]
