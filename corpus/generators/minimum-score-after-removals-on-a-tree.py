import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        v, e = kw["nums"], kw["edges"]
        n = len(v)
        assert 3 <= n <= 1000 and all(1 <= x <= 10**8 for x in v)
        assert len(e) == n - 1 and all(
            len(edge) == 2 and 0 <= min(edge) < max(edge) < n for edge in e
        )
        # Independently validate connectivity, including the original examples' edge orientations.
        adj = [[] for _ in v]
        for a, b in e:
            adj[a].append(b)
            adj[b].append(a)
        visited = {0}
        stack = [0]
        while stack:
            for nxt in adj[stack.pop()]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        assert len(visited) == n
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"nums": [1, 5, 5, 4, 11], "edges": [[0, 1], [1, 2], [1, 3], [3, 4]]},
        {"nums": [5, 5, 2, 4, 4, 2], "edges": [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]},
    ] + [
        {"nums": [10**8] * 1000, "edges": [[i - 1, i] for i in range(1, 1000)]},
        {"nums": [1] * 1000, "edges": [[0, i] for i in range(1, 1000)]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(3, 18)
        v = [rng.randint(1, 100) for _ in range(n)]
        if len(calls) % 4 == 0:
            v = [rng.randint(1, 100)] * n
        if len(calls) % 3 == 0:
            e = [[0, i] for i in range(1, n)]
        elif len(calls) % 3 == 1:
            e = [[i - 1, i] for i in range(1, n)]
        else:
            e = [[rng.randrange(i), i] for i in range(1, n)]
        add(nums=v, edges=e)
    return calls
