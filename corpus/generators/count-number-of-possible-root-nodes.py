import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        edges, guesses, k = kwargs["edges"], kwargs["guesses"], kwargs["k"]
        n = len(edges) + 1
        assert 2 <= n <= 100000 and all(
            0 <= a < n and 0 <= b < n and a != b for a, b in edges
        )
        assert 1 <= len(guesses) <= 100000 and len(set(map(tuple, guesses))) == len(
            guesses
        )
        edge_set = {tuple(sorted(e)) for e in edges}
        assert all(tuple(sorted(e)) in edge_set for e in guesses) and 0 <= k <= len(
            guesses
        )
        parent = list(range(n))

        def find(v: int) -> int:
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        for a, b in edges:
            ra, rb = find(a), find(b)
            assert ra != rb, "A valid tree cannot contain a cycle or repeated edge."
            parent[ra] = rb
        assert len(edges) == n - 1 and len({find(v) for v in range(n)}) == 1
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        edges=[[v, v - 1] for v in range(1, 100000)],
        guesses=[[v - 1, v] for v in range(1, 100000)] + [[1, 0]],
        k=50000,
    )
    add(
        edges=[[0, 1], [1, 2], [1, 3], [4, 2]],
        guesses=[[1, 3], [0, 1], [1, 0], [2, 4]],
        k=3,
    )
    add(
        edges=[[0, 1], [1, 2], [2, 3], [3, 4]],
        guesses=[[1, 0], [3, 4], [2, 1], [3, 2]],
        k=1,
    )
    while len(calls) < 600:
        n = rng.randint(2, 50)
        edges = [[v, rng.randrange(v)] for v in range(1, n)]
        labels = list(range(n))
        rng.shuffle(labels)
        edges = [[labels[a], labels[b]] for a, b in edges]
        options = [e for a, b in edges for e in [(a, b), (b, a)]]
        guesses = [list(e) for e in rng.sample(options, rng.randint(1, len(options)))]
        add(edges=edges, guesses=guesses, k=rng.randint(0, len(guesses)))
    return calls
