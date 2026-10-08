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
        r = k["restrictions"]
        assert 2 <= n <= 10**9 and 0 <= len(r) <= min(n - 1, 100000)
        assert len({a for a, b in r}) == len(r) and all(
            2 <= a <= n and 0 <= b <= 10**9 for a, b in r
        )

    add(n=5, restrictions=[[2, 1], [4, 1]])
    add(n=6, restrictions=[])
    add(n=10, restrictions=[[5, 3], [2, 5], [7, 4], [10, 3]])
    add(n=10**9, restrictions=[])
    add(n=10**9, restrictions=[[i, 0 if i % 2 else 10**9] for i in range(2, 100002)])
    add(n=10**9, restrictions=[[10**9, 0]])
    while len(calls) < 600:
        n = rng.randint(2, 100)
        r = [
            [i, rng.randrange(n + 1)]
            for i in rng.sample(range(2, n + 1), rng.randrange(min(n, 25)))
        ]
        add(n=n, restrictions=r)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
