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
        assert 1 <= k["targetX"] <= 10**9 and 1 <= k["targetY"] <= 10**9

    add(targetX=6, targetY=9)
    add(targetX=4, targetY=7)
    for a, b in [
        (1, 1),
        (10**9, 10**9),
        (10**9, 1),
        (2**29, 2**29),
        (999999999, 999999999),
    ]:
        add(targetX=a, targetY=b)
    while len(calls) < 600:
        if len(calls) % 2:
            g = 1 << rng.randrange(20)
            a = rng.randint(1, 10**9 // g)
            b = a + 1 if a < 10**9 // g else 1
            add(targetX=a * g, targetY=b * g)
        else:
            g = rng.choice([3, 5, 7, 9, 15])
            add(
                targetX=g * rng.randint(1, 10**9 // g),
                targetY=g * rng.randint(1, 10**9 // g),
            )
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
