import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(grid):
        key = tuple(map(tuple, grid))
        if key not in seen:
            assert 1 <= len(grid) <= 300 and 1 <= len(grid[0]) <= 300
            assert all(len(row) == len(grid[0]) and set(row) <= {0, 1} for row in grid)
            seen.add(key)
            cases.append(f"candidate(grid={grid!r})")

    add([[0]])
    add([[1]])
    for _ in range(300):
        m = r.randint(1, 30)
        n = r.randint(1, 30)
        base = [r.randrange(2) for _ in range(n)]
        grid = [base[:] if r.randrange(2) else [1 - v for v in base] for _ in range(m)]
        add(grid)
    for _ in range(300):
        m = r.randint(2, 30)
        n = r.randint(2, 30)
        grid = [[r.randrange(2) for _ in range(n)] for _ in range(m)]
        # Force incompatible rows, which cannot be made identical by column flips.
        grid[0] = [0] * n
        grid[1] = [0] * (n - 1) + [1]
        add(grid)
    add(
        [
            [i % 2 for i in range(300)]
            if j % 2 == 0
            else [1 - i % 2 for i in range(300)]
            for j in range(300)
        ]
    )
    add([[0] * 300, [0] * 299 + [1]] + [[0] * 300 for _ in range(298)])
    return cases
