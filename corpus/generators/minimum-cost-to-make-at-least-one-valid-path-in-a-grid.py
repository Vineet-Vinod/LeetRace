import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        assert (
            1 <= len(g) <= 100
            and 1 <= len(g[0]) <= 100
            and all(
                len(row) == len(g[0]) and all(1 <= v <= 4 for v in row) for row in g
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

    add(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]])
    add(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]])
    add(grid=[[1, 2], [4, 3]])
    add(grid=[[2] * 100 for _ in range(100)])
    add(grid=[[1] * 100 for _ in range(100)])
    t = 0
    while len(calls) < 600:
        r, c = rng.randint(1, 10), rng.randint(1, 10)
        grid = [[rng.randint(1, 4) for _ in range(c)] for _ in range(r)]
        if t % 4 == 0:
            grid[0] = [1] * c
            for row in grid:
                row[-1] = 3
        add(grid=grid)
        t += 1
    return calls
