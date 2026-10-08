import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        n = len(g)
        assert (
            2 <= n <= 100
            and all(len(row) == n and all(v in (0, 1) for v in row) for row in g)
            and g[0][0] == g[0][1] == 0
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

    add(
        grid=[
            [0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
        ]
    )
    add(
        grid=[
            [0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 0],
        ]
    )
    add(grid=[[0] * 100 for _ in range(100)])
    add(grid=[[0, 0] + [1] * 98] + [[1] * 100 for _ in range(99)])
    t = 0
    while len(calls) < 600:
        n = rng.randint(2, 12)
        prob = rng.choice([0.05, 0.2, 0.4, 0.7])
        g = [[int(rng.random() < prob) for _ in range(n)] for _ in range(n)]
        g[0][0] = g[0][1] = 0
        if t % 3 == 0:
            for row in g:
                row[0] = row[1] = 0
            g[-1] = [0] * n
        add(grid=g)
        t += 1
    return calls
