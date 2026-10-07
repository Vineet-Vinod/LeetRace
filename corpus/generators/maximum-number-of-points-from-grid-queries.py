import random


def sample(r, turn):
    m, n = r.randint(2, 8), r.randint(2, 8)
    g = [[r.randint(1, 25) for _ in range(n)] for _ in range(m)]
    q = [r.choice([1, 26, g[0][0], r.randint(1, 30)]) for _ in range(r.randint(1, 30))]
    return dict(grid=g, queries=q)


def validate(grid, queries):
    m, n = len(grid), len(grid[0])
    assert (
        2 <= m <= 1000
        and 2 <= n <= 1000
        and 4 <= m * n <= 100000
        and all(len(row) == n for row in grid)
    )
    assert (
        all(1 <= v <= 10**6 for row in grid for v in row)
        and 1 <= len(queries) <= 10000
        and all(1 <= q <= 10**6 for q in queries)
    )


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    calls = []
    seen = set()

    def add(**kwargs):
        validate(**kwargs)
        parts = []
        for key, value in kwargs.items():
            expression = repr(value)
            parts.append(key + "=" + expression)
        call = "candidate(" + ", ".join(parts) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(grid=[[1, 2, 3], [2, 5, 7], [3, 5, 1]], queries=[5, 6, 2])
    add(grid=[[5, 2, 1], [1, 1, 2]], queries=[3])
    add(grid=[[10**6] * 1000 for _ in range(100)], queries=[1, 10**6] * 5000)
    add(grid=[[1] * 100 for _ in range(1000)], queries=[2])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
