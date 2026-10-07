import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        n = d["n"]
        e = d["edges"]
        assert (
            1 <= n <= 30000
            and len(e) == n - 1
            and all(
                len(p) == 2 and 0 <= p[0] < n and 0 <= p[1] < n and p[0] != p[1]
                for p in e
            )
        )
        p = list(range(n))

        def root(v):
            while p[v] != v:
                p[v] = p[p[v]]
                v = p[v]
            return v

        for u, v in e:
            u, v = root(u), root(v)
            assert u != v
            p[u] = v
        # An acyclic n-1-edge graph is a tree.

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

    add(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
    add(n=1, edges=[])
    add(n=2, edges=[[1, 0]])
    add(n=30000, edges=[[i - 1, i] for i in range(1, 30000)])
    add(n=30000, edges=[[0, i] for i in range(1, 30000)])
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 45)
        e = [[i, rng.randrange(i)] for i in range(1, n)]
        if t % 3 == 0:
            e = [[0, i] for i in range(1, n)]
        if t % 3 == 1:
            e = [[i - 1, i] for i in range(1, n)]
        rng.shuffle(e)
        add(n=n, edges=e)
        t += 1
    return calls
