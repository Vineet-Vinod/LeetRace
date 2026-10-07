import random


def generate(seed: int = 0) -> list[str]:
    """Generate rectangular grids of dimensions 1..300 with street types 1..6."""
    rng = random.Random(seed)
    calls = {
        "candidate(grid=[[2, 4, 3], [6, 5, 2]])",
        "candidate(grid=[[1, 2, 1], [1, 2, 1]])",
        "candidate(grid=[[1] * 300])",
        "candidate(grid=[[2] for _ in range(300)])",
        "candidate(grid=[[1] * 299 + [3]] + [[1] * 299 + [2] for _ in range(299)])",
    }
    while len(calls) < 600:
        rows, cols = rng.randint(1, 40), rng.randint(1, 40)
        if rng.random() < 0.55:
            grid = [[rng.randint(1, 6) for _ in range(cols)] for _ in range(rows)]
        else:
            grid = [[1] * cols for _ in range(rows)]
            if rows == 1:
                pass
            elif cols == 1:
                grid = [[2] for _ in range(rows)]
            else:
                grid[0][-1] = 3
                for row in range(1, rows):
                    grid[row][-1] = 2
        assert 1 <= len(grid) <= 300 and 1 <= len(grid[0]) <= 300
        assert all(
            len(row) == len(grid[0]) and all(1 <= cell <= 6 for cell in row)
            for row in grid
        )
        calls.add(f"candidate(grid={grid!r})")
    return sorted(calls)
