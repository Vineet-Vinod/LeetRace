import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        g, k = args["grid"], args["k"]
        m, n = len(g), len(g[0])
        assert 1 <= m <= 40 and 1 <= n <= 40 and 1 <= k <= m * n
        assert all(len(row) == n and all(x in (0, 1) for x in row) for row in g)
        assert g[0][0] == g[-1][-1] == 0
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1)
    add(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1)
    g = [[1] * 40 for _ in range(40)]
    g[0][0] = g[-1][-1] = 0
    add(grid=g, k=1)
    add(grid=g, k=1600)
    add(grid=g, k=76)
    add(grid=[[0]], k=1)
    add(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1)
    while len(calls) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        g = [[rng.randint(0, 1) for _ in range(n)] for _ in range(m)]
        g[0][0] = g[-1][-1] = 0
        kind = len(calls) % 3
        if kind == 0:
            k = rng.randint(1, m * n)
        elif kind == 1:
            m, n = rng.randint(2, 18), rng.randint(2, 18)
            k = 1
            g = [[1] * n for _ in range(m)]
            g[0][0] = g[-1][-1] = 0
        else:
            k = 1
            g[0] = [0] * n
            for row in g:
                row[-1] = 0
        add(grid=g, k=k)
    return list(calls)[:600]
