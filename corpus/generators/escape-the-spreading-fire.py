import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        g = args["grid"]
        m, n = len(g), len(g[0])
        assert 2 <= m <= 300 and 2 <= n <= 300 and 4 <= m * n <= 20000
        assert all(len(row) == n and all(x in (0, 1, 2) for x in row) for row in g)
        assert g[0][0] == g[-1][-1] == 0
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(
        grid=[
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 1, 0],
            [0, 2, 0, 0, 1, 2, 0],
            [0, 0, 2, 2, 2, 0, 2],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    )
    add(grid=[[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]])
    add(grid=[[0, 0, 0], [2, 2, 0], [1, 2, 0]])
    base = [
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 1, 0],
        [0, 2, 0, 0, 1, 2, 0],
        [0, 0, 2, 2, 2, 0, 2],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    add(grid=base)
    # Extending the sole exit corridor preserves the finite waiting-time example.
    for m in range(5, 15):
        for n in range(7, 19):
            g = [row + [2] * (n - 7) for row in base]
            g[-1] = g[-1][:7] + [0] * (n - 7)
            g += [[2] * (n - 1) + [0] for _ in range(m - 5)]
            add(grid=g)
    add(grid=[[0] * 2 for _ in range(300)])
    add(
        grid=[
            [0, 0, 0, 0, 2],
            [0, 0, 2, 2, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 2, 0, 2, 0],
            [0, 0, 0, 2, 1],
            [0, 0, 2, 0, 2],
            [2, 0, 0, 0, 0],
        ]
    )
    add(
        grid=[
            [0, 0, 0, 2, 0],
            [0, 2, 1, 0, 0],
            [0, 2, 2, 2, 0],
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [0, 0, 0, 2, 2],
            [0, 2, 0, 0, 0],
        ]
    )
    add(
        grid=[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 0, 1],
            [0, 0, 2, 2, 0, 2, 2],
            [0, 0, 0, 2, 2, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 2, 0, 0, 2, 0],
        ]
    )
    add(grid=[[0, 0, 0, 0], [0, 2, 0, 0], [1, 0, 2, 0]])
    add(
        grid=[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 2, 2],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 2, 0],
            [1, 2, 0, 2, 2, 0, 0],
        ]
    )
    add(
        grid=[
            [0, 0, 0, 2, 2, 0, 0],
            [0, 2, 0, 0, 0, 0, 2],
            [0, 0, 2, 2, 0, 0, 2],
            [0, 0, 2, 0, 0, 0, 0],
            [2, 0, 1, 2, 2, 2, 0],
        ]
    )
    add(grid=[[0] * 200 for _ in range(100)])
    add(grid=[[0] * 300 for _ in range(2)])
    add(grid=[[0, 0], [0, 0]])
    while len(calls) < 600:
        m, n = rng.randint(2, 12), rng.randint(2, 12)
        kind = len(calls) % 4
        g = [
            [rng.choices([0, 1, 2], weights=[6, 1, 3])[0] for _ in range(n)]
            for _ in range(m)
        ]
        if kind == 0:
            g = [[rng.choice([0, 2]) for _ in range(n)] for _ in range(m)]
            g[0] = [0] * n
            g[-1] = [0] * n
            [row.__setitem__(0, 0) for row in g]
        if kind == 1:
            g[0][1] = 1
            g[1][0] = 1
        g[0][0] = g[-1][-1] = 0
        add(grid=g)
    return list(calls)[:600]
