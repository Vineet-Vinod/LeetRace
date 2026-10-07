import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(edges, n, k):
        key = (tuple(map(tuple, edges)), n, k)
        if key not in seen:
            assert 1 <= n <= 100 and 1 <= k <= n and 1 <= len(edges) <= 6000
            assert all(
                1 <= u <= n and 1 <= v <= n and u != v and 0 <= w <= 100
                for u, v, w in edges
            )
            assert len({(u, v) for u, v, _ in edges}) == len(edges)
            seen.add(key)
            cases.append(f"candidate(times={edges!r}, n={n}, k={k})")

    for _ in range(300):
        n = r.randint(2, 80)
        k = 1
        edges = [[i, i + 1, r.randint(0, 20)] for i in range(1, n)]
        for _ in range(r.randint(0, n)):
            u = r.randint(1, n)
            v = r.randint(1, n)
            if u != v and not any(e[0] == u and e[1] == v for e in edges):
                edges.append([u, v, r.randint(0, 100)])
        add(edges, n, k)
    for _ in range(300):
        n = r.randint(2, 80)
        edges = [[i, i + 1, r.randint(0, 100)] for i in range(2, n)]
        if not edges:
            edges = [[2, 1, r.randint(0, 100)]]
        add(edges, n, 1)
    add([[i, i + 1, 1] for i in range(1, 100)], 100, 1)
    add([[i, i + 1, 100] for i in range(1, 100)], 100, 1)
    add([[i, i + 1, 1] for i in range(2, 100)], 100, 1)
    return cases
