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
        assert 3 <= n <= 50
        for i, ns in enumerate(graph):
            assert 1 <= len(ns) < n and len(ns) == len(set(ns))
            assert all(0 <= j < n and j != i and i in graph[j] for j in ns)
            if i:
                assert any(
                    j != 0 for j in ns
                )  # Cat has a legal move from every non-hole node.

    add(graph=[[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]])
    add(graph=[[1, 3], [0, 2], [1, 3], [0, 2]])
    while len(calls) < 599:
        mode = len(calls) % 3
        n = rng.randint(7, 18) if mode == 2 else rng.randint(5, 11)
        g = [set() for _ in range(n)]

        def edge(a, b):
            g[a].add(b)
            g[b].add(a)

        if mode == 0:
            edge(0, 1)
            for i in range(1, n):
                edge(i, 1 + i % (n - 1))
        elif mode == 1:
            edge(1, 2)
            edge(0, 3)
            edge(2, 4)
            edge(3, 4)
            for i in range(5, n):
                edge(i, rng.randrange(2, i))
        else:
            edge(0, 3)
            edge(3, 4)
            edge(1, 5)
            edge(2, 6)
            for i in range(7, n):
                edge(i, rng.choice([1, 5]))
        for i in range(n):
            for j in range(i + 1, n):
                if mode < 2 and rng.random() < 0.15:
                    edge(i, j)
                elif (
                    mode == 2
                    and i not in {0, 2, 3, 4, 6}
                    and j not in {0, 2, 3, 4, 6}
                    and rng.random() < 0.2
                ):
                    edge(i, j)
        if any(not ns for ns in g) or any(
            not any(x for x in g[i]) for i in range(1, n)
        ):
            continue
        add(graph=[sorted(ns) for ns in g])
    # A 50-node cycle reaches the actual node bound.
    add(graph=[sorted({(i - 1) % 50, (i + 1) % 50}) for i in range(50)])
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
