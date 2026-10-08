import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        g = kw["grid"]
        m, n = len(g), len(g[0])
        assert 1 <= m <= 1000 and 1 <= n <= 1000 and m * n <= 100000
        assert all(len(row) == n and all(1 <= v <= 100000 for v in row) for row in g)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"grid": [[1, 1], [3, 4]]}, {"grid": [[1], [2]]}] + [
        {"grid": [[1] * 1000 for _ in range(100)]},
        {"grid": [[i * 100 + j + 1 for j in range(100)] for i in range(1000)]},
        {"grid": [[100000]]},
    ]:
        add(**kw)
    while len(calls) < 600:
        m, n = rng.randint(1, 10), rng.randint(1, 10)
        g = [[rng.randint(1, 30) for _ in range(n)] for _ in range(m)]
        if len(calls) % 4 == 0:
            g = [[rng.randint(1, 100000)] * n for _ in range(m)]
        if len(calls) % 4 == 1:
            offset = rng.randint(1, 90000)
            g = [[offset + i * n + j for j in range(n)] for i in range(m)]
        add(grid=g)
    return calls
