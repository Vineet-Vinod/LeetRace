import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        rows, cols = 1 + rng.randrange(20), 1 + rng.randrange(20)
        value = rng.randint(1, 10**6)
        grid = [[value] * cols for _ in range(rows)]
        calls.add(f"candidate(grid={grid!r})")
    for case in range(300):
        rows, cols = 1 + rng.randrange(20), 1 + rng.randrange(20)
        grid = [[rng.randint(1, 10**6) for _ in range(cols)] for _ in range(rows)]
        calls.add(f"candidate(grid={grid!r})")
    calls.add(f"candidate(grid={[[10**6] * 50 for _ in range(50)]!r})")
    grid = [[row * 50 + col + 1 for col in range(50)] for row in range(50)]
    calls.add(f"candidate(grid={grid!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(grid=[[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]])",
    "candidate(grid=[[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
