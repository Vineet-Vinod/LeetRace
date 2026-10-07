import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(n=30, queries=[[1, 2**30 - 1] for _ in range(100000)])
    while len(calls) < 600:
        n = rng.randint(2, 30)
        queries = []
        for _ in range(rng.randint(1, 25)):
            a, b = rng.sample(range(1, 2**n), 2)
            queries.append([a, b])
        assert all(1 <= a < 2**n and 1 <= b < 2**n and a != b for a, b in queries)
        add(n=n, queries=queries)
    assert len(calls) == 600
    return list(calls)
