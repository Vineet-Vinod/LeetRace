import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        g = kw["matrix"]
        m, n = len(g), len(g[0])
        assert 1 <= m <= 500 and 1 <= n <= 500
        assert all(
            len(row) == n and all(-(10**9) <= v <= 10**9 for v in row) for row in g
        )
        # The minimum feasible ranks are uniquely determined for every integer matrix.
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"matrix": [[1, 2], [3, 4]]},
        {"matrix": [[7, 7], [7, 7]]},
        {"matrix": [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]},
    ] + [
        {"matrix": [[10**9] * 500 for _ in range(500)]},
        {"matrix": [[-(10**9)]]},
        {"matrix": [[i * 500 + j for j in range(500)] for i in range(500)]},
    ]:
        add(**kw)
    while len(calls) < 600:
        m, n = rng.randint(1, 8), rng.randint(1, 8)
        g = [[rng.randint(-10, 10) for _ in range(n)] for _ in range(m)]
        if len(calls) % 4 == 0:
            g = [[rng.randint(-(10**9), 10**9)] * n for _ in range(m)]
        if len(calls) % 4 == 1:
            g = [[rng.randint(-(10**9), 10**9) for _ in range(n)] for _ in range(m)]
        add(matrix=g)
    return calls
