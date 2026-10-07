import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(n=1, edges=[], queries=[[0, 0]])
    add(
        n=10000,
        edges=[[i - 1, i, i % 26 + 1] for i in range(1, 10000)],
        queries=[[0, i % 10000] for i in range(20000)],
    )
    while len(calls) < 600:
        n = rng.randint(2, 45)
        edges = [[rng.randrange(i), i, rng.randint(1, 26)] for i in range(1, n)]
        if len(calls) % 4 == 0:
            for e in edges:
                e[2] = 1
        queries = [
            [rng.randrange(n), rng.randrange(n)] for _ in range(rng.randint(1, 25))
        ]
        assert (
            len(edges) == n - 1
            and 1 <= len(queries) <= 20000
            and all(1 <= w <= 26 for _, _, w in edges)
        )
        add(n=n, edges=edges, queries=queries)
    assert len(calls) == 600
    return list(calls)
