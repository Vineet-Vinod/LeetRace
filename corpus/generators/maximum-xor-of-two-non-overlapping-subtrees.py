import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(n, edges, values):
        assert (
            2 <= n <= 50000
            and len(edges) == n - 1
            and len(values) == n
            and all(1 <= v <= 10**9 for v in values)
        )
        # Parent smaller than child and every nonroot attached once imply a tree rooted at 0.
        assert all(0 <= a < b < n for a, b in edges) and sorted(
            b for a, b in edges
        ) == list(range(1, n))

    add(n=6, edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], values=[2, 8, 3, 6, 2, 5])
    while len(calls) < 598:
        n = rng.randint(2, 35)
        mode = len(calls) % 3
        edges = [
            [rng.randrange(i) if mode == 0 else (0 if mode == 1 else i - 1), i]
            for i in range(1, n)
        ]
        add(
            n=n,
            edges=edges,
            values=[rng.randint(1, 10**9 if mode == 0 else 30) for _ in range(n)],
        )
    calls[
        "candidate(n=50000, edges=[[i-1,i] for i in range(1,50000)], values=[1000000000]*50000)"
    ] = None
    calls[
        "candidate(n=50000, edges=[[0,i] for i in range(1,50000)], values=[1]*50000)"
    ] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
