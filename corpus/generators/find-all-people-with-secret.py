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
        m = k["meetings"]
        assert 2 <= n <= 10**5 and 1 <= len(m) <= 10**5 and 1 <= k["firstPerson"] < n
        assert all(
            len(e) == 3
            and 0 <= e[0] < n
            and 0 <= e[1] < n
            and e[0] != e[1]
            and 1 <= e[2] <= 10**5
            for e in m
        )

    add(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1)
    add(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3)
    add(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1)
    add(
        n=100000,
        meetings=[[i - 1, i, 100000] for i in range(1, 100000)] + [[0, 99999, 1]],
        firstPerson=1,
    )
    add(n=100000, meetings=[[99998, 99999, 100000]], firstPerson=1)
    while len(calls) < 600:
        n = rng.randint(2, 35)
        m = []
        for _ in range(rng.randint(1, 80)):
            a, b = rng.sample(range(n), 2)
            m.append([a, b, rng.randint(1, 8)])
        add(n=n, meetings=m, firstPerson=rng.randrange(1, n))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
