import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(maxTime, edges, passingFees):
        n = len(passingFees)
        if not (
            1 <= maxTime <= 1000
            and 2 <= n <= 1000
            and n - 1 <= len(edges) <= 1000
            and all(1 <= f <= 1000 for f in passingFees)
            and all(
                len(e) == 3
                and 0 <= e[0] < n
                and 0 <= e[1] < n
                and e[0] != e[1]
                and 1 <= e[2] <= 1000
                for e in edges
            )
        ):
            return False
        adj = [[] for _ in range(n)]
        for a, b, t in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen = {0}
        todo = [0]
        for u in todo:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        return len(seen) == n

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for t in [30, 29, 25]:
        emit(
            maxTime=t,
            edges=[
                [0, 1, 10],
                [1, 2, 10],
                [2, 5, 10],
                [0, 3, 1],
                [3, 4, 10],
                [4, 5, 15],
            ],
            passingFees=[5, 1, 2, 20, 20, 3],
        )
    emit(
        maxTime=1000,
        edges=[[i, i + 1, 1] for i in range(999)] + [[0, 999, 1000]],
        passingFees=[1000] * 1000,
    )
    while len(calls) < 600:
        n = rng.randint(2, 16)
        edges = [[i, rng.randrange(i), rng.randint(1, 20)] for i in range(1, n)]
        for _ in range(rng.randint(0, 20)):
            a, b = rng.sample(range(n), 2)
            edges.append([a, b, rng.randint(1, 30)])
        fees = [rng.randint(1, 1000) for _ in range(n)]
        emit(
            maxTime=rng.choice([1, 1000, rng.randint(2, 80)]),
            edges=edges,
            passingFees=fees,
        )
    assert len(calls) == 600
    return list(calls)
