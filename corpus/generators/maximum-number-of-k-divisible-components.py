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
        values = k["values"]
        div = k["k"]
        assert (
            1 <= n <= 30000
            and len(values) == n
            and all(0 <= x <= 10**9 for x in values)
            and 1 <= div <= 10**9
            and sum(values) % div == 0
        )
        valid_tree(n, k["edges"])

    add(n=5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6)
    add(
        n=7,
        edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
        values=[3, 0, 6, 1, 5, 2, 1],
        k=3,
    )
    add(
        n=30000,
        edges=[[i - 1, i] for i in range(1, 30000)],
        values=[10**9] * 30000,
        k=10**9,
    )
    add(n=30000, edges=[[0, i] for i in range(1, 30000)], values=[0] * 30000, k=1)
    while len(calls) < 600:
        n = rng.randint(1, 35)
        div = rng.randint(1, 30)
        values = [rng.randrange(60) for _ in range(n - 1)]
        values.append((-sum(values)) % div)
        add(n=n, edges=tree(n, len(calls) % 3), values=values, k=div)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
