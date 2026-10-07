"""Every generated matrix is square and has values in 1..n."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)

    def is_valid(matrix: list[list[int]]) -> bool:
        size = len(matrix)
        expected = set(range(1, size + 1))
        return all(set(row) == expected for row in matrix) and all(
            {matrix[row][column] for row in range(size)} == expected
            for column in range(size)
        )

    valid_cases = set()
    invalid_cases = set()
    while len(valid_cases) < 300 or len(invalid_cases) < 300:
        size = rng.randint(2, 30)
        symbols = list(range(1, size + 1))
        offsets = list(range(size))
        columns = list(range(size))
        rng.shuffle(symbols)
        rng.shuffle(offsets)
        rng.shuffle(columns)
        matrix = [
            [symbols[(offsets[row] + columns[column]) % size] for column in range(size)]
            for row in range(size)
        ]
        if len(valid_cases) < 300:
            valid_cases.add(f"candidate(matrix={matrix!r})")
        if len(invalid_cases) < 300:
            broken = [row.copy() for row in matrix]
            broken[0][0] = broken[0][1]
            invalid_cases.add(f"candidate(matrix={broken!r})")
    assert all(is_valid(ast_literal_matrix(call)) for call in valid_cases)
    assert all(not is_valid(ast_literal_matrix(call)) for call in invalid_cases)
    return sorted(valid_cases | invalid_cases)


def ast_literal_matrix(call: str) -> list[list[int]]:
    import ast

    return ast.literal_eval(call.split("matrix=", 1)[1][:-1])


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(matrix=[[(i + j) % 100 + 1 for j in range(100)] for i in range(100)])",
            "candidate(matrix=[[1] * 100] + [[(i + j) % 100 + 1 for j in range(100)] for i in range(1, 100)])",
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(matrix=[[1]])",
            "candidate(matrix=[[1, 2], [2, 1]])",
            "candidate(matrix=[[1, 1], [1, 1]])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
