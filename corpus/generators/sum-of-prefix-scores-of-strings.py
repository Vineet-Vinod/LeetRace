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
        assert 1 <= len(k["words"]) <= 1000 and all(
            1 <= len(w) <= 1000 and lower(w) for w in k["words"]
        )

    add(words=["abc", "ab", "bc", "b"])
    add(words=["abcd"])
    add(words=["a" * 1000] * 1000)
    add(words=[chr(97 + i % 26) * 1000 for i in range(1000)])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        prefix = letters(rng.randint(1, 8)) if len(calls) % 3 else ""
        add(
            words=[
                prefix
                + letters(
                    rng.randint(1, 15),
                    rng.choice(["ab", "abc", "abcdefghijklmnopqrstuvwxyz"]),
                )
                for _ in range(n)
            ]
        )
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
