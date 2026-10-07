import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        r, c = len(g), len(g[0])
        assert (
            2 <= r <= 1000 and 2 <= c <= 1000 and 4 <= r * c <= 100000 and g[0][0] == 0
        )
        assert all(len(row) == c and all(0 <= v <= 100000 for v in row) for row in g)

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

    add(grid=[[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]])
    add(grid=[[0, 2, 4], [3, 2, 1], [1, 0, 4]])
    g = [[100000] * 100 for _ in range(1000)]
    g[0][0] = 0
    g[0][1] = 1
    add(grid=g)
    g = [[0] * 1000 for _ in range(100)]
    add(grid=g)
    t = 0
    while len(calls) < 600:
        r, c = rng.randint(2, 10), rng.randint(2, 10)
        g = [[rng.randint(0, 100) for _ in range(c)] for _ in range(r)]
        g[0][0] = 0
        if t % 3:
            g[0][1] = rng.randint(0, 1)
        if t % 4 == 0:
            for j in range(c):
                g[0][j] = j
            for i in range(r):
                g[i][-1] = c - 1 + i
        add(grid=g)
        t += 1
    return calls
