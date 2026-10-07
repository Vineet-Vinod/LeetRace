import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        h, c, m, n, t = (data[x] for x in ["houses", "cost", "m", "n", "target"])
        assert 1 <= m <= 100 and 1 <= n <= 20 and 1 <= t <= m and len(h) == len(c) == m
        assert all(0 <= x <= n for x in h) and all(
            len(row) == n and all(1 <= v <= 10000 for v in row) for row in c
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {
            "houses": [0, 0, 0, 0, 0],
            "cost": [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            "m": 5,
            "n": 2,
            "target": 3,
        },
        {
            "houses": [0, 2, 1, 2, 0],
            "cost": [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            "m": 5,
            "n": 2,
            "target": 3,
        },
        {
            "houses": [3, 1, 2, 3],
            "cost": [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
            "m": 4,
            "n": 3,
            "target": 3,
        },
    ]:
        add(**example)
    add(
        houses=[0] * 100,
        cost=[[10000] * 20 for _ in range(100)],
        m=100,
        n=20,
        target=100,
    )
    add(houses=[0] * 100, cost=[[1] * 20 for _ in range(100)], m=100, n=20, target=1)
    add(houses=[1] * 100, cost=[[10000] for _ in range(100)], m=100, n=1, target=100)
    while len(calls) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 5)
        h = [rng.randrange(n + 1) for _ in range(m)]
        mode = len(calls) % 3
        if mode == 0:
            h = [0] * m
        if mode == 1:
            h = [rng.randint(1, n) for _ in range(m)]
        t = rng.randint(1, m)
        if mode == 1 and len(calls) % 2 == 0:
            t = 1 + sum(h[i] != h[i - 1] for i in range(1, m))
        c = [[rng.randint(1, 10000) for _ in range(n)] for _ in range(m)]
        add(houses=h, cost=c, m=m, n=n, target=t)
    assert len(calls) == 600
    return calls
