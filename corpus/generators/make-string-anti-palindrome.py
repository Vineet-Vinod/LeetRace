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
        assert 2 <= len(k["s"]) <= 100000 and len(k["s"]) % 2 == 0 and lower(k["s"])

    add(s="abca")
    add(s="abba")
    add(s="cccd")
    add(s="a" * 50000 + "b" * 50000)
    add(s="a" * 50001 + "b" * 49999)
    add(s=("abcdefghijklmnopqrstuvwxyz" * 3847)[:100000])
    while len(calls) < 600:
        n = 2 * rng.randint(1, 45)
        if len(calls) % 3:
            s = letters(n, rng.choice(["abc", "abcd", "abcdefghijklmnopqrstuvwxyz"]))
        else:
            s = "a" * (n // 2 + 1) + letters(n // 2 - 1, "bc")
        add(s=s)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
