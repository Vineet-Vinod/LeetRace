import random
import string


def encode_diagonals(text: str, rows: int) -> str:
    cols = len(text) // rows
    matrix = [[" "] * cols for _ in range(rows)]
    index = 0
    for start_col in range(cols):
        row, col = 0, start_col
        while row < rows and col < cols:
            matrix[row][col] = text[index]
            index += 1
            row += 1
            col += 1
    return "".join("".join(row) for row in matrix)


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: encoded text length 0..1000000; 1..1000 rows; generated nonempty cases encode full valid rectangular plaintexts."""
    rng = random.Random(seed)
    calls = {
        "candidate(encodedText='ch   ie   pr', rows=3)",
        "candidate(encodedText='coding', rows=1)",
        "candidate(encodedText='', rows=3)",
    }
    while len(calls) < 600:
        rows, cols = rng.randint(1, 10), rng.randint(1, 15)
        text = "".join(rng.choice(string.ascii_lowercase) for _ in range(rows * cols))
        encoded = encode_diagonals(text, rows)
        calls.add(f"candidate(encodedText={encoded!r}, rows={rows})")
    return sorted(calls)
