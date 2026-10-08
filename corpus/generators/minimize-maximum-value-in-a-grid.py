import random


def sample(r, turn):
    m, n = r.randint(1, 8), r.randint(1, 8)
    a = r.sample(range(1, 10000), m * n)
    return dict(grid=[a[i * n : (i + 1) * n] for i in range(m)])


def validate(grid):
    m, n = len(grid), len(grid[0])
    a = [v for row in grid for v in row]
    assert (
        1 <= m <= 1000
        and 1 <= n <= 1000
        and 1 <= m * n <= 100000
        and all(len(row) == n for row in grid)
    )
    assert len(set(a)) == m * n and all(1 <= v <= 10**9 for v in a)


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

    add(grid=[[3, 1], [2, 5]])
    add(grid=[[10]])
    add(grid=[[10**9 - r * 1000 - c for c in range(1000)] for r in range(100)])
    add(grid=[[r * 100 + c + 1 for c in range(100)] for r in range(1000)])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
