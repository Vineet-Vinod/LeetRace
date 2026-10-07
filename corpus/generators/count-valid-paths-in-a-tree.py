import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(n, edges):
        assert 1 <= n <= 100000 and len(edges) == n - 1
        # Each vertex attaches once to an earlier vertex, proving connectedness and acyclicity.
        assert all(1 <= a < b <= n for a, b in edges) and sorted(
            b for a, b in edges
        ) == list(range(2, n + 1))

    add(n=1, edges=[])
    add(n=5, edges=[[1, 2], [1, 3], [2, 4], [2, 5]])
    attempt = 0
    while len(calls) < 598:
        attempt += 1
        n = rng.randint(2, 70)
        mode = attempt % 3
        edges = [
            [rng.randint(1, i - 1) if mode == 0 else (1 if mode == 1 else i - 1), i]
            for i in range(2, n + 1)
        ]
        add(n=n, edges=edges)
    calls["candidate(n=100000, edges=[[i,i+1] for i in range(1,100000)])"] = None
    calls["candidate(n=100000, edges=[[1,i] for i in range(2,100001)])"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
