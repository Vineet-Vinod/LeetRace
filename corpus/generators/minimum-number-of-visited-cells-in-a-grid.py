import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        grid = kwargs["grid"]
        m = len(grid)
        n = len(grid[0])
        assert 1 <= m <= 100000 and 1 <= n <= 100000 and m * n <= 100000
        assert (
            all(len(row) == n and all(0 <= v < m * n for v in row) for row in grid)
            and grid[-1][-1] == 0
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(grid=[[99999] * 99999 + [0]])
    add(grid=[[1] for _ in range(99999)] + [[0]])
    add(grid=[[499] * 200 for _ in range(500 - 1)] + [[499] * 199 + [0]])
    add(grid=[[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]])
    add(grid=[[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]])
    add(grid=[[2, 1, 0], [1, 0, 0]])
    while len(calls) < 600:
        m = rng.randint(1, 12)
        n = rng.randint(1, 12)
        mode = rng.randrange(4)
        grid = [[rng.randrange(m * n) for _ in range(n)] for _ in range(m)]
        if mode == 0:
            grid = [[rng.randrange(min(3, m * n)) for _ in range(n)] for _ in range(m)]
        if mode == 1:
            grid = [[1 if m * n > 1 else 0] * n for _ in range(m)]
        grid[-1][-1] = 0
        add(grid=grid)
    return calls
