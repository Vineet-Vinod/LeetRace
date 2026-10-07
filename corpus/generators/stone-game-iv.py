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
        assert 1 <= k["n"] <= 100000

    add(n=1)
    add(n=2)
    add(n=4)
    add(n=100000)
    add(n=99999)
    add(n=1)
    add(n=2)
    add(n=4)
    # Classify a modest legal domain to construct many winning and losing starts.
    winning = [False] * 5001
    for n in range(1, 5001):
        winning[n] = any(not winning[n - r * r] for r in range(1, int(n**0.5) + 1))
    positive = [n for n in range(1, 5001) if winning[n]]
    negative = [n for n in range(1, 5001) if not winning[n]]
    for n in range(1, 251):
        add(n=n)
    while len(calls) < 600:
        add(n=rng.choice(positive if len(calls) % 2 else negative))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
