import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        n = d["n"]
        e = d["edges"]
        assert 3 <= n <= 100000 and len(e) == n
        assert all(
            len(p) == 2 and 0 <= p[0] < n and 0 <= p[1] < n and p[0] != p[1] for p in e
        )
        assert len({tuple(sorted(p)) for p in e}) == n
        # Connected simple graph with n edges has exactly one cycle.
        g = [[] for _ in range(n)]
        for u, v in e:
            g[u].append(v)
            g[v].append(u)
        seen = {0}
        todo = [0]
        for u in todo:
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        assert len(seen) == n

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=7, edges=[[1, 2], [2, 4], [4, 3], [3, 1], [0, 1], [5, 2], [6, 5]])
    add(
        n=9,
        edges=[[0, 1], [1, 2], [0, 2], [2, 6], [6, 7], [6, 8], [0, 3], [3, 4], [3, 5]],
    )
    add(
        n=100000,
        edges=[[0, 1], [1, 2], [2, 0]] + [[i - 1, i] for i in range(3, 100000)],
    )
    t = 0
    while len(calls) < 600:
        n = rng.randint(3, 35)
        cycle = rng.randint(3, n)
        e = [[i, (i + 1) % cycle] for i in range(cycle)] + [
            [i, rng.randrange(i)] for i in range(cycle, n)
        ]
        labels = list(range(n))
        rng.shuffle(labels)
        e = [[labels[u], labels[v]] for u, v in e]
        rng.shuffle(e)
        add(n=n, edges=e)
        t += 1
    return calls
