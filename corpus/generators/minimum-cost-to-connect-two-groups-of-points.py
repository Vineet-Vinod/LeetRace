import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        cost = kwargs["cost"]
        m = len(cost)
        n = len(cost[0])
        assert 1 <= n <= m <= 12 and all(len(row) == n for row in cost)
        assert all(0 <= v <= 100 for row in cost for v in row)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(cost=[[100] * 12 for _ in range(12)])
    add(cost=[[0 if i == j else 100 for j in range(12)] for i in range(12)])
    add(cost=[[15, 96], [36, 2]])
    add(cost=[[1, 3, 5], [4, 1, 1], [1, 5, 3]])
    add(cost=[[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]])
    while len(calls) < 600:
        m = rng.randint(1, 7)
        n = rng.randint(1, m)
        cost = [[rng.randint(0, 100) for _ in range(n)] for _ in range(m)]
        if len(calls) % 4 == 0:
            for row in cost:
                row[rng.randrange(n)] = 0
        add(cost=cost)
    return calls
