import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]])",
            "candidate(n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]])",
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

    def values(a, lo, hi, minimum=1, maximum=100000):
        assert minimum <= len(a) <= maximum and all(lo <= x <= hi for x in a)

    def validate(p):
        n = p["n"]
        assert 1 <= n <= 50
        graph_valid(n, p["edges"], n - 1, n - 1, True)
        values(p["price"], 2, 1000, n, n)
        assert all(x % 2 == 0 for x in p["price"])
        assert 1 <= len(p["trips"]) <= 100 and all(
            len(t) == 2 and all(0 <= x < n for x in t) for t in p["trips"]
        )

    add(
        n=50,
        edges=[[i, i + 1] for i in range(49)],
        price=[1000] * 50,
        trips=[[0, 49]] * 100,
    )
    add(n=1, edges=[], price=[2], trips=[[0, 0]])
    attempts = 0
    while len(calls) < 600:
        attempts % 8
        attempts += 1
        n = rng.randint(1, 18)
        add(
            n=n,
            edges=tree(n),
            price=[2 * rng.randint(1, 500) for _ in range(n)],
            trips=[
                [rng.randrange(n), rng.randrange(n)] for _ in range(rng.randint(1, 30))
            ],
        )
    return list(calls)
