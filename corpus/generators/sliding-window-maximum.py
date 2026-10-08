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
        assert (
            1 <= len(k["nums"]) <= 100000
            and 1 <= k["k"] <= len(k["nums"])
            and all(-10000 <= x <= 10000 for x in k["nums"])
        )

    add(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
    add(nums=[1], k=1)
    add(nums=[-10000, 10000] * 50000, k=1)
    add(nums=[i % 20001 - 10000 for i in range(100000)], k=50000)
    add(nums=[-10000] * 100000, k=100000)
    while len(calls) < 600:
        n = rng.randint(1, 100)
        a = [rng.randint(-20, 20) for _ in range(n)]
        if len(calls) % 4 == 0:
            a.sort()
        if len(calls) % 4 == 1:
            a.sort(reverse=True)
        add(nums=a, k=rng.randint(1, n))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
