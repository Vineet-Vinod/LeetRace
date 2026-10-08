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
        a = k["locations"]
        assert (
            2 <= len(a) <= 100
            and len(set(a)) == len(a)
            and all(1 <= x <= 10**9 for x in a)
        )
        assert (
            0 <= k["start"] < len(a)
            and 0 <= k["finish"] < len(a)
            and 1 <= k["fuel"] <= 200
        )

    add(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5)
    add(locations=[4, 3, 1], start=1, finish=0, fuel=6)
    add(locations=[5, 2, 1], start=0, finish=2, fuel=3)
    add(locations=list(range(1, 101)), start=0, finish=99, fuel=200)
    add(locations=[1, 10**9], start=0, finish=1, fuel=200)
    while len(calls) < 600:
        n = rng.randint(2, 12)
        a = rng.sample(range(1, 60), n)
        start = rng.randrange(n)
        finish = start if len(calls) % 4 == 0 else rng.randrange(n)
        fuel = rng.randint(1, 60)
        add(locations=a, start=start, finish=finish, fuel=fuel)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
