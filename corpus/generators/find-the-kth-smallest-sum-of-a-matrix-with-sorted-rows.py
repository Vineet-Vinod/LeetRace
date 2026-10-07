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
        mat = k["mat"]
        m = len(mat)
        n = len(mat[0])
        assert (
            1 <= m <= 40
            and 1 <= n <= 40
            and all(
                len(r) == n and r == sorted(r) and all(1 <= x <= 5000 for x in r)
                for r in mat
            )
        )
        assert 1 <= k["k"] <= min(200, n**m)

    add(mat=[[1, 3, 11], [2, 4, 6]], k=5)
    add(mat=[[1, 3, 11], [2, 4, 6]], k=9)
    add(mat=[[1, 10, 10], [1, 4, 5], [2, 3, 6]], k=7)
    add(mat=[[5000] * 40 for _ in range(40)], k=200)
    add(mat=[list(range(1, 41)) for _ in range(40)], k=200)
    while len(calls) < 600:
        m = rng.randint(1, 6)
        n = rng.randint(1, 8)
        mat = [sorted(rng.randint(1, 25) for _ in range(n)) for _ in range(m)]
        add(mat=mat, k=rng.randint(1, min(200, n**m)))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
