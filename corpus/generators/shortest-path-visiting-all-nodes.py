import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(graph):
        n = len(graph)
        assert 1 <= n <= 12
        assert all(
            len(ns) < n
            and len(ns) == len(set(ns))
            and all(0 <= u < n and u != i and i in graph[u] for u in ns)
            for i, ns in enumerate(graph)
        )
        reached = {0}
        stack = [0]
        while stack:
            for u in graph[stack.pop()]:
                if u not in reached:
                    reached.add(u)
                    stack.append(u)
        assert len(reached) == n

    add(graph=[[]])
    add(graph=[[1, 2, 3], [0], [0], [0]])
    while len(calls) < 597:
        n = rng.randint(2, 9)
        g = [set() for _ in range(n)]
        for i in range(1, n):
            p = rng.randrange(i)
            g[p].add(i)
            g[i].add(p)
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < 0.15:
                    g[i].add(j)
                    g[j].add(i)
        add(graph=[sorted(ns) for ns in g])
    add(graph=[[j for j in range(12) if j != i] for i in range(12)])
    add(graph=[list(range(1, 12))] + [[0] for _ in range(11)])
    add(graph=[[j for j in [i - 1, i + 1] if 0 <= j < 12] for i in range(12)])
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
