import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        grid = [[rng.choice(["X", "O"]) for _ in range(cols)] for _ in range(rows)]
        start = (rng.randrange(rows), rng.randrange(cols))
        grid[start[0]][start[1]] = "*"
        if rows * cols > 1 and rng.random() < 0.75:
            food = (rng.randrange(rows), rng.randrange(cols))
            while food == start:
                food = (rng.randrange(rows), rng.randrange(cols))
            grid[food[0]][food[1]] = "#"
        calls.add(f"candidate(grid={grid!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(grid=[['X', 'X', 'X', 'X', 'X', 'X'], ['X', '*', 'O', 'O', 'O', 'X'], ['X', 'O', 'O', '#', 'O', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']])",
    "candidate(grid=[['X', 'X', 'X', 'X', 'X'], ['X', '*', 'X', 'O', 'X'], ['X', 'O', 'X', '#', 'X'], ['X', 'X', 'X', 'X', 'X']])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
