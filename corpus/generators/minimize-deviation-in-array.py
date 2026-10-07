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
        assert 2 <= len(k["nums"]) <= 50000 and all(1 <= x <= 10**9 for x in k["nums"])

    add(nums=[1, 2, 3, 4])
    add(nums=[4, 1, 5, 20, 3])
    add(nums=[2, 10, 8])
    add(nums=[10**9] * 50000)
    add(nums=[1, 999999999] * 25000)
    add(nums=[2**29] * 50000)
    while len(calls) < 600:
        n = rng.randint(2, 40)
        if len(calls) % 4 == 0:
            odd = rng.randrange(1, 30, 2)
            a = [odd * 2 ** rng.randrange(8) for _ in range(n)]
        else:
            a = [rng.randint(1, 1000) for _ in range(n)]
        add(nums=a)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
