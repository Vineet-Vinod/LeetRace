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
        f = k["flowers"]
        p = k["people"]
        assert 1 <= len(f) <= 50000 and all(
            len(e) == 2 and 1 <= e[0] <= e[1] <= 10**9 for e in f
        )
        assert 1 <= len(p) <= 50000 and all(1 <= x <= 10**9 for x in p)

    add(flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], people=[2, 3, 7, 11])
    add(flowers=[[1, 10], [3, 3]], people=[3, 3, 2])
    add(flowers=[[1, 10**9]] * 50000, people=[1, 10**9] * 25000)
    add(flowers=[[i, i] for i in range(1, 50001)], people=list(range(1, 50001)))
    while len(calls) < 600:
        f = [
            sorted([rng.randint(1, 60), rng.randint(1, 60)])
            for _ in range(rng.randint(1, 45))
        ]
        p = [rng.randint(1, 70) for _ in range(rng.randint(1, 45))]
        if len(calls) % 3 == 0:
            p.extend([f[0][0], f[0][1]])
        add(flowers=f, people=p)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
