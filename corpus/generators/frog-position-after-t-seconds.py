import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        n, edges, t, target = (data[x] for x in ["n", "edges", "t", "target"])
        assert (
            1 <= n <= 100 and len(edges) == n - 1 and 1 <= t <= 50 and 1 <= target <= n
        )
        parent = list(range(n + 1))

        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for edge in edges:
            assert len(edge) == 2
            u, v = edge
            assert 1 <= u <= n and 1 <= v <= n and root(u) != root(v)
            parent[root(u)] = root(v)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 2,
            "target": 4,
        },
        {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 1,
            "target": 7,
        },
    ]:
        add(**example)
    add(n=1, edges=[], t=50, target=1)
    add(n=100, edges=[[i, i + 1] for i in range(1, 100)], t=50, target=51)
    add(n=100, edges=[[1, i] for i in range(2, 101)], t=50, target=100)
    while len(calls) < 600:
        n = rng.randint(2, 100)
        mode = len(calls) % 3
        edges = [
            [(i - 1 if mode == 0 else 1 if mode == 1 else rng.randrange(1, i)), i]
            for i in range(2, n + 1)
        ]
        target = rng.randint(1, n)
        depth = [0] * (n + 1)
        for u, v in edges:
            depth[v] = depth[u] + 1
        # Half the cases hit the target at its arrival time, others probe departures/staying.
        t = (
            max(1, min(50, depth[target]))
            if len(calls) % 2 == 0
            else rng.randint(1, 50)
        )
        add(n=n, edges=edges, t=t, target=target)
    assert len(calls) == 600
    return calls
