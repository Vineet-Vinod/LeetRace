import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]])",
            "candidate(nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])",
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
        n = len(p["nums"])
        values(p["nums"], 1, 50)
        graph_valid(n, p["edges"], n - 1, n - 1, True)

    add(nums=[50] * 100000, edges=[[i, i + 1] for i in range(99999)])
    add(nums=[1] * 100000, edges=[[0, i] for i in range(1, 100000)])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 70)
        a = [rng.randint(1, 50) for _ in range(n)]
        if mode == 0:
            a = [rng.choice([1, 2, 3, 5, 7, 11])] * n
        if mode == 1:
            a = [rng.choice([2, 4, 6, 8, 10]) for _ in range(n)]
        add(nums=a, edges=tree(n))
    return list(calls)
