import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        g, k = kwargs["matrix"], kwargs["k"]
        assert 1 <= len(g) <= 100 and 1 <= len(g[0]) <= 100
        assert all(
            len(row) == len(g[0]) and all(-100 <= x <= 100 for x in row) for row in g
        )
        assert -100000 <= k <= 100000
        # A cell witnesses feasibility, or the full matrix does.
        assert min(min(row) for row in g) <= k or sum(map(sum, g)) <= k
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(matrix=[[1, 0, 1], [0, -2, 3]], k=2)
    add(matrix=[[2, 2, -1]], k=3)
    add(matrix=[[100] * 100 for _ in range(100)], k=100000)
    add(matrix=[[-100] * 100 for _ in range(100)], k=-100000)
    add(matrix=[[100]], k=100000)
    add(matrix=[[-100]], k=-100)
    while len(calls) < 600:
        m, n = rng.randint(1, 7), rng.randint(1, 7)
        g = [[rng.randint(-100, 100) for _ in range(n)] for _ in range(m)]
        k = rng.randint(min(min(row) for row in g), 300)
        add(matrix=g, k=k)
    return calls
