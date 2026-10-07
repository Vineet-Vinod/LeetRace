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
        w = k["words"]
        t = k["target"]
        assert (
            1 <= len(w) <= 1000
            and 1 <= len(w[0]) <= 1000
            and all(len(s) == len(w[0]) and lower(s) for s in w)
        )
        assert 1 <= len(t) <= 1000 and lower(t)

    add(words=["acca", "bbbb", "caca"], target="aba")
    add(words=["abba", "baab"], target="bab")
    add(words=["a" * 1000] * 1000, target="a" * 1000)
    add(words=["a"], target="b" * 1000)
    while len(calls) < 600:
        n = rng.randint(1, 12)
        width = rng.randint(1, 22)
        words = [letters(width) for _ in range(n)]
        length = rng.randint(1, width + 3)
        if len(calls) % 2 and length <= width:
            positions = sorted(rng.sample(range(width), length))
            target = "".join(rng.choice(words)[i] for i in positions)
        else:
            target = letters(length, "abcd")
        add(words=words, target=target)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
