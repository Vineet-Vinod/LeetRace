import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        validate(kw)
        call = "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kw.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(n, alphabet="abc"):
        return "".join(rng.choice(alphabet) for _ in range(n))

    def tree(n, mode=0):
        edges = [
            [i, i - 1 if mode == 1 else 0 if mode == 2 else rng.randrange(i)]
            for i in range(1, n)
        ]
        labels = list(range(n))
        rng.shuffle(labels)
        edges = [[labels[a], labels[b]] for a, b in edges]
        rng.shuffle(edges)
        return edges

    def valid_tree(n, edges):
        assert len(edges) == n - 1
        parents = list(range(n))

        def root(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        for a, b in edges:
            assert 0 <= a < n and 0 <= b < n and root(a) != root(b)
            parents[root(a)] = root(b)

    def lower(s):
        return all("a" <= c <= "z" for c in s)

    def validate(k):
        n = k["n"]
        assert 1 <= n <= 10**9
        assert len(k["lamps"]) <= 20000 and len(k["queries"]) <= 20000
        assert all(
            len(p) == 2 and all(0 <= v < n for v in p)
            for p in k["lamps"] + k["queries"]
        )

    add(n=5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 0]])
    add(n=5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 1]])
    add(n=5, lamps=[[0, 0], [0, 4]], queries=[[0, 4], [0, 1], [1, 4]])
    add(
        n=10**9,
        lamps=[[i, 10**9 - 1 - i] for i in range(20000)],
        queries=[[i, 10**9 - 1 - i] for i in range(20000)],
    )
    add(n=1, lamps=[], queries=[])
    add(n=1, lamps=[[0, 0]] * 20000, queries=[[0, 0]] * 20000)
    while len(calls) < 600:
        n = rng.randint(1, 30)
        lamps = [[rng.randrange(n), rng.randrange(n)] for _ in range(rng.randrange(40))]
        queries = [
            [rng.randrange(n), rng.randrange(n)] for _ in range(rng.randrange(40))
        ]
        add(n=n, lamps=lamps, queries=queries)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
