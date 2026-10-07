import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate symmetric valid squares, self-conjugate ragged squares, and one-cell invalid variants."""
    rng = random.Random(seed)
    valid = set()
    invalid = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def make_square() -> tuple[str, ...]:
        size = rng.randint(2, 15)
        diagonal_count = rng.randint(1, size)
        arms = sorted(rng.sample(range(size), diagonal_count), reverse=True)
        cells: set[tuple[int, int]] = set()
        for diagonal, arm_length in enumerate(arms):
            for offset in range(arm_length + 1):
                position = diagonal + offset
                cells.add((diagonal, position))
                cells.add((position, diagonal))
        extent = max(row for row, _ in cells) + 1
        matrix = [[""] * extent for _ in range(extent)]
        for row, column in sorted(cells):
            if matrix[row][column]:
                continue
            char = rng.choice(alphabet)
            matrix[row][column] = char
            matrix[column][row] = char
        lengths = [
            max(column for cell_row, column in cells if cell_row == row) + 1
            for row in range(extent)
        ]
        return tuple("".join(matrix[row][: lengths[row]]) for row in range(extent))

    while len(valid) < 300 or len(invalid) < 300:
        square = make_square()
        off_diagonal = [
            (row, column)
            for row in range(len(square))
            for column in range(row + 1, len(square[row]))
        ]
        if not off_diagonal:
            continue
        if len(valid) < 300:
            valid.add(square)
        if len(invalid) < 300:
            broken = [list(word) for word in square]
            row, column = rng.choice(off_diagonal)
            broken[row][column] = rng.choice(
                [char for char in alphabet if char != broken[row][column]]
            )
            invalid.add(tuple("".join(word) for word in broken))

    cases = (
        valid
        | invalid
        | {
            ("abcd", "bnrt", "crmy", "dtye"),
            ("abcd", "bnrt", "crm", "dt"),
            ("abc", "bcd", "cd", "d"),
            ("ball", "area", "lead", "lady"),
            ("a",),
            tuple("a" * 500 for _ in range(500)),
        }
    )
    generated_calls = [f"candidate(words={list(words)!r})" for words in cases]
    example_calls = ["candidate(words=['ball', 'area', 'read', 'lady'])"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
