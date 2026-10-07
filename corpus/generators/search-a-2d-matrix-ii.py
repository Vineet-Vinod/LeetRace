import random


def generate(seed: int = 0) -> list[str]:
    """Use monotone matrices and balance targets chosen inside and outside each matrix."""
    rng = random.Random(seed)
    boundary = [
        [row * 3_000_000 + col * 10_000 for col in range(300)] for row in range(300)
    ]
    calls = [f"candidate(matrix={boundary!r}, target={boundary[-1][-1]})"]
    seen: set[str] = set(calls)
    index = 0
    while len(calls) < 600:
        rows = 1 + index % 12
        cols = 1 + (index * 7) % 12
        matrix = [
            [row * 100 + col * 10 + rng.randrange(10) for col in range(cols)]
            for row in range(rows)
        ]
        if index % 2 == 0:
            target = matrix[rng.randrange(rows)][rng.randrange(cols)]
        else:
            target = rng.randrange(-1000, rows * 100 + cols * 10 + 100)
        assert all(all(row[i] < row[i + 1] for i in range(cols - 1)) for row in matrix)
        assert all(
            matrix[row][col] < matrix[row + 1][col]
            for row in range(rows - 1)
            for col in range(cols)
        )
        call = f"candidate(matrix={matrix!r}, target={target})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
