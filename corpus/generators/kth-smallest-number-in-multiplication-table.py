import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        m, n, k = args["m"], args["n"], args["k"]
        assert 1 <= m <= 30000 and 1 <= n <= 30000 and 1 <= k <= m * n
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(m=3, n=3, k=5)
    add(m=2, n=3, k=6)
    add(m=30000, n=30000, k=900000000)
    add(m=30000, n=30000, k=450000000)
    add(m=1, n=30000, k=30000)
    add(m=3, n=3, k=5)
    add(m=2, n=3, k=6)
    while len(calls) < 600:
        m, n = rng.randint(1, 70), rng.randint(1, 70)
        add(m=m, n=n, k=rng.choice([1, m * n, rng.randint(1, m * n)]))
    return list(calls)[:600]
