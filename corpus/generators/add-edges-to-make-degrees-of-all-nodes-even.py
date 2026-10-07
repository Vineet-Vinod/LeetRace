import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        n, edges = kwargs["n"], kwargs["edges"]
        assert 3 <= n <= 100000 and 2 <= len(edges) <= 100000
        assert all(1 <= a <= n and 1 <= b <= n and a != b for a, b in edges)
        assert len({tuple(sorted(e)) for e in edges}) == len(edges)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=100000, edges=[[i, i + 1] for i in range(1, 100000)])
    add(n=100000, edges=[[1, i] for i in range(2, 100001)] + [[2, 3]])
    add(n=3, edges=[[1, 2], [2, 3]])
    add(n=5, edges=[[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]])
    add(n=4, edges=[[1, 2], [3, 4]])
    add(n=4, edges=[[1, 2], [1, 3], [1, 4]])
    while len(calls) < 600:
        n = rng.randint(3, 35)
        pairs = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1)]
        edges = [
            list(e) for e in rng.sample(pairs, rng.randint(2, min(len(pairs), 50)))
        ]
        if rng.randrange(3) == 0:
            # A random cycle gives a substantial family with all degrees even.
            vertices = rng.sample(range(1, n + 1), rng.randint(3, n))
            edges = [
                [vertices[j], vertices[(j + 1) % len(vertices)]]
                for j in range(len(vertices))
            ]
        add(n=n, edges=edges)
    return calls
