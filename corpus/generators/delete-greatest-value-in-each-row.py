import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        row_count = rng.randint(1, 50)
        column_count = rng.randint(1, 50)
        grid = [
            [rng.randint(1, 100) for _ in range(column_count)] for _ in range(row_count)
        ]
        assert all(
            len(row) == column_count and all(1 <= value <= 100 for value in row)
            for row in grid
        )
        calls.add(f"candidate(grid={grid!r})")
    return sorted(calls)
