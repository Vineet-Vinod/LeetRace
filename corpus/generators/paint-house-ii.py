import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["costs"]
        n, k = len(a), len(a[0])
        assert 1 <= n <= 100 and 2 <= k <= 20
        assert all(len(row) == k and all(1 <= v <= 20 for v in row) for row in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(costs=[[1, 5, 3], [2, 9, 4]])
    add(costs=[[1, 3], [2, 4]])
    add(costs=[[20] * 20 for _ in range(100)])
    add(costs=[[1] * 2 for _ in range(100)])
    add(costs=[[1, 5, 3], [2, 9, 4]])
    while len(calls) < 600:
        n, k = rng.randint(1, 20), rng.randint(2, 20)
        add(costs=[[rng.randint(1, 20) for _ in range(k)] for _ in range(n)])
    return list(calls)[:600]
