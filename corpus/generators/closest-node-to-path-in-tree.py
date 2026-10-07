import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(n=1, edges=[], query=[[0, 0, 0]])
    add(
        n=1000,
        edges=[[i - 1, i] for i in range(1, 1000)],
        query=[[0, 999, i] for i in range(1000)],
    )
    while len(calls) < 600:
        n = rng.randint(2, 35)
        # Attach each new vertex to an earlier one, proving connectedness and acyclicity.
        edges = [[rng.randrange(i), i] for i in range(1, n)]
        query = [
            [rng.randrange(n) for _ in range(3)] for _ in range(rng.randint(1, 25))
        ]
        assert len(edges) == n - 1 and 1 <= len(query) <= 1000
        add(n=n, edges=edges, query=query)
    assert len(calls) == 600
    return list(calls)
