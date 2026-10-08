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
        g = k["group"]
        p = k["profit"]
        assert (
            1 <= k["n"] <= 100
            and 0 <= k["minProfit"] <= 100
            and 1 <= len(g) <= 100
            and len(g) == len(p)
        )
        assert all(1 <= x <= 100 for x in g) and all(0 <= x <= 100 for x in p)

    add(n=5, minProfit=3, group=[2, 2], profit=[2, 3])
    add(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8])
    add(n=100, minProfit=100, group=[1] * 100, profit=[100] * 100)
    add(n=100, minProfit=0, group=[1] * 100, profit=[0] * 100)
    add(n=1, minProfit=100, group=[100] * 100, profit=[100] * 100)
    while len(calls) < 600:
        size = rng.randint(1, 18)
        n = rng.randint(1, 30)
        g = [rng.randint(1, 15) for _ in range(size)]
        p = [rng.randint(0, 20) for _ in range(size)]
        add(n=n, minProfit=rng.choice([0, rng.randint(1, 50)]), group=g, profit=p)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
