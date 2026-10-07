import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        assert (
            1 <= len(g) <= 10000
            and 1 <= len(g[0]) <= 5
            and all(
                len(row) == len(g[0]) and all(v in (0, 1) for v in row) for row in g
            )
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(grid=[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]])
    add(grid=[[0]])
    add(grid=[[1, 1, 1], [1, 1, 1]])
    add(grid=[[1, 1, 1, 1, 1]] * 9998 + [[1, 0, 0, 0, 0], [0, 1, 1, 1, 1]])
    add(grid=[[1] * 5] * 9999 + [[0] * 5])
    add(grid=[[1, 0], [0, 1], [0, 0]])
    t = 0
    while len(calls) < 600:
        rows, cols = rng.randint(1, 25), rng.randint(1, 5)
        grid = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
        if t % 3 == 0:
            grid[rng.randrange(rows)] = [0] * cols
        if t % 3 == 1:
            for row in grid:
                row[0] = 1
        add(grid=grid)
        t += 1
    return calls
