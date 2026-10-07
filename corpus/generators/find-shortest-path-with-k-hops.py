import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        n, edges, s, d, k = (data[x] for x in ["n", "edges", "s", "d", "k"])
        assert 2 <= n <= 500 and n - 1 <= len(edges) <= min(10000, n * (n - 1) // 2)
        assert 0 <= s < n and 0 <= d < n and s != d and 0 <= k < n
        pairs = set()
        graph = [[] for _ in range(n)]
        for edge in edges:
            assert len(edge) == 3
            u, v, w = edge
            assert 0 <= u < n and 0 <= v < n and u != v and 1 <= w <= 1000000
            pair = tuple(sorted([u, v]))
            assert pair not in pairs
            pairs.add(pair)
            graph[u].append(v)
            graph[v].append(u)
        reached = {0}
        queue = [0]
        for u in queue:
            for v in graph[u]:
                if v not in reached:
                    reached.add(v)
                    queue.append(v)
        assert len(reached) == n
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"n": 4, "edges": [[0, 1, 4], [0, 2, 2], [2, 3, 6]], "s": 1, "d": 3, "k": 2},
        {
            "n": 7,
            "edges": [
                [3, 1, 9],
                [3, 2, 4],
                [4, 0, 9],
                [0, 5, 6],
                [3, 6, 2],
                [6, 0, 4],
                [1, 2, 4],
            ],
            "s": 4,
            "d": 1,
            "k": 2,
        },
        {
            "n": 5,
            "edges": [[0, 4, 2], [0, 1, 3], [0, 2, 1], [2, 1, 4], [1, 3, 4], [3, 4, 7]],
            "s": 2,
            "d": 3,
            "k": 1,
        },
    ]:
        add(**example)
    add(n=500, edges=[[i - 1, i, 1000000] for i in range(1, 500)], s=0, d=499, k=499)
    add(n=500, edges=[[i - 1, i, 1000000] for i in range(1, 500)], s=0, d=499, k=0)
    # Exactly 10000 unique edges, with the star guaranteeing connectivity.
    edges = [[0, i, 1000000] for i in range(1, 500)]
    for u in range(1, 500):
        for v in range(u + 1, 500):
            if len(edges) < 10000:
                edges.append([u, v, 1])
    add(n=500, edges=edges, s=1, d=499, k=1)
    while len(calls) < 600:
        n = rng.randint(2, 18)
        edges = [[rng.randrange(i), i, rng.randint(1, 1000000)] for i in range(1, n)]
        pairs = {tuple(sorted(e[:2])) for e in edges}
        for _ in range(n):
            u, v = rng.sample(range(n), 2)
            pair = tuple(sorted([u, v]))
            if pair not in pairs:
                pairs.add(pair)
                edges.append([u, v, rng.randint(1, 1000000)])
        s, d = rng.sample(range(n), 2)
        add(n=n, edges=edges, s=s, d=d, k=rng.choice([0, 1, n - 1, rng.randrange(n)]))
    assert len(calls) == 600
    return calls
