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
        t = k["target"]
        d = k["dictionary"]
        m = len(t)
        n = len(d)
        assert 1 <= m <= 21 and lower(t) and 0 <= n <= 1000 and t not in d
        assert all(1 <= len(w) <= 100 and lower(w) for w in d)
        assert n == 0 or n <= 2 ** (21 - m)

    add(target="apple", dictionary=["blade"])
    add(target="apple", dictionary=["blade", "plain", "amber"])
    add(target="abcdefghijklmnopqrstu", dictionary=[])
    add(target="abcdefghijklmnopqrstu", dictionary=["bbcdefghijklmnopqrstu"])
    add(target="a" * 11, dictionary=["b" * 11] * 1000)
    add(target="a", dictionary=["b" * 100])
    while len(calls) < 600:
        m = rng.randint(1, 10)
        t = letters(m)
        d = []
        for _ in range(rng.randint(0, 12)):
            w = letters(m if rng.randrange(4) else rng.randint(1, 12))
            if w != t:
                d.append(w)
        add(target=t, dictionary=d)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
