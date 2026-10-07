import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]])",
            "candidate(n = 3, edges = [[1,2],[2,3],[3,1]])",
        ]
    )

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        calls[ast.unparse(ast.parse(call, mode="eval"))] = None

    def tree(n):
        return [[rng.randrange(i), i] for i in range(1, n)]

    def connected(n, extra=0):
        edges = {tuple(edge) for edge in tree(n)}
        while len(edges) < min(n * (n - 1) // 2, n - 1 + extra):
            a, b = sorted(rng.sample(range(n), 2))
            edges.add((a, b))
        return [[a + 1, b + 1] for a, b in sorted(edges)]

    def graph_valid(n, edges, minimum, maximum, connected_required=False, offset=0):
        assert minimum <= len(edges) <= maximum
        pairs = {tuple(sorted(edge)) for edge in edges}
        assert len(pairs) == len(edges)
        assert all(
            len(edge) == 2
            and edge[0] != edge[1]
            and all(offset <= x < n + offset for x in edge)
            for edge in edges
        )
        if connected_required:
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a - offset].append(b - offset)
                adj[b - offset].append(a - offset)
            seen = {0}
            queue = [0]
            for u in queue:
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            assert len(seen) == n

    def validate(p):
        assert 1 <= p["n"] <= 500
        graph_valid(p["n"], p["edges"], 1, 10000, offset=1)

    add(n=500, edges=[[i, i + 1] for i in range(1, 500)])
    add(n=500, edges=[[a, b] for a in range(1, 101) for b in range(101, 201)])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(2, 20)
        if mode < 4:
            cut = rng.randint(1, n - 1)
            edges = [
                [a, b]
                for a in range(1, cut + 1)
                for b in range(cut + 1, n + 1)
                if rng.random() < 0.35
            ]
            if not edges:
                edges = [[1, n]]
        else:
            edges = connected(n, rng.randint(0, n))
        add(n=n, edges=edges)
    return list(calls)
