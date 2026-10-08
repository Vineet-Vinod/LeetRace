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
        n = len(k["edges"]) + 1
        assert 2 <= n <= 100000
        valid_tree(n, k["edges"])

    add(edges=[[0, 1], [0, 2]])
    add(edges=[[0, 1]])
    add(edges=[[2, 4], [0, 1], [2, 3], [0, 2]])
    add(edges=[[i - 1, i] for i in range(1, 100000)])
    add(edges=[[0, i] for i in range(1, 100000)])
    while len(calls) < 600:
        n = rng.randint(2, 80)
        add(edges=tree(n, len(calls) % 3))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
