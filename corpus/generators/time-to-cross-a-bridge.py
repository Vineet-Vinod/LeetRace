import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(n, k, time):
        assert 1 <= n <= 10000 and 1 <= k <= 10000 and len(time) == k
        assert all(len(t) == 4 and all(1 <= v <= 1000 for v in t) for t in time)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("n", n),
                    ("k", k),
                    ("time", time),
                )
            )
            + ")"
        )
        calls[call] = None

    add(n=1, k=3, time=[[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]])
    add(n=3, k=2, time=[[1, 5, 1, 8], [10, 10, 10, 10]])
    add(n=10000, k=10000, time=[[1000] * 4 for _ in range(10000)])
    add(n=10000, k=1, time=[[1, 1000, 1, 1000]])
    add(n=1, k=1, time=[[1] * 4])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        k = rng.randint(1, 15)
        mode = rng.randrange(4)
        if mode == 0:
            # Equal crossing sums force the worker-index priority rule.
            right = rng.randint(1, 30)
            left = rng.randint(1, 30)
            time = [
                [right, rng.randint(1, 50), left, rng.randint(1, 50)] for _ in range(k)
            ]
        elif mode == 1:
            time = [
                [
                    rng.randint(1, 10),
                    rng.randint(100, 1000),
                    rng.randint(1, 10),
                    rng.randint(100, 1000),
                ]
                for _ in range(k)
            ]
        else:
            time = [[rng.randint(1, 50) for _ in range(4)] for _ in range(k)]
        add(n=n, k=k, time=time)
    return list(calls)
