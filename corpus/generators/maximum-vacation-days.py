import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        f, d = args["flights"], args["days"]
        n = len(f)
        k = len(d[0])
        assert 1 <= n <= 100 and 1 <= k <= 100 and len(d) == n
        assert all(len(row) == n and all(x in (0, 1) for x in row) for row in f)
        assert all(f[i][i] == 0 for i in range(n))
        assert all(len(row) == k and all(0 <= x <= 7 for x in row) for row in d)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(
        flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]],
        days=[[1, 3, 1], [6, 0, 3], [3, 3, 3]],
    )
    add(
        flights=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        days=[[1, 1, 1], [7, 7, 7], [7, 7, 7]],
    )
    add(
        flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]],
        days=[[7, 0, 0], [0, 7, 0], [0, 0, 7]],
    )
    add(
        flights=[[int(i != j) for j in range(100)] for i in range(100)],
        days=[[7] * 100 for _ in range(100)],
    )
    add(flights=[[0]], days=[[0]])
    add(flights=[[0]], days=[[7] * 100])
    while len(calls) < 600:
        n, k = rng.randint(1, 8), rng.randint(1, 12)
        f = [[0 if i == j else rng.randint(0, 1) for j in range(n)] for i in range(n)]
        if len(calls) % 3 == 0:
            f = [[0] * n for _ in range(n)]
        add(flights=f, days=[[rng.randint(0, 7) for _ in range(k)] for _ in range(n)])
    return list(calls)[:600]
