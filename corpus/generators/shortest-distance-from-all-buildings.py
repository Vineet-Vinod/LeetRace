import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        grid = kwargs["grid"]
        m = len(grid)
        n = len(grid[0])
        assert 1 <= m <= 50 and 1 <= n <= 50 and all(len(row) == n for row in grid)
        assert all(v in (0, 1, 2) for row in grid for v in row) and any(
            1 in row for row in grid
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        grid=[
            [1 if i in (0, 49) or j in (0, 49) else 0 for j in range(50)]
            for i in range(50)
        ]
    )
    add(grid=[[1] * 50 for _ in range(50)])
    add(grid=[[1] + [0] * 49] + [[0] * 50 for _ in range(49)])
    add(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
    add(grid=[[1, 0]])
    add(grid=[[1]])
    while len(calls) < 600:
        m = rng.randint(1, 9)
        n = rng.randint(1, 9)
        mode = rng.randrange(3)
        if mode == 0:
            grid = [[0] * n for _ in range(m)]
            for _ in range(rng.randint(1, min(m * n, 6))):
                grid[rng.randrange(m)][rng.randrange(n)] = 1
        else:
            grid = [
                [rng.choices([0, 1, 2], weights=[5, 2, 3])[0] for _ in range(n)]
                for _ in range(m)
            ]
        grid[rng.randrange(m)][rng.randrange(n)] = 1
        add(grid=grid)
    return calls
