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
        num = k["num"]
        assert (
            1 <= len(num) <= 30000
            and (num == "0" or num[0] != "0")
            and all("0" <= c <= "9" for c in num)
        )
        assert 1 <= k["k"] <= 10**9

    add(num="4321", k=4)
    add(num="100", k=1)
    add(num="36789", k=1000)
    add(num="0", k=1)
    add(num="9876543210" * 3000, k=10**9)
    add(num="1" + "0" * 29999, k=1)
    add(num="9" * 15000 + "0" * 15000, k=10**7)
    while len(calls) < 600:
        n = rng.randint(1, 45)
        num = rng.choice("123456789") + "".join(
            rng.choice("0123456789") for _ in range(n - 1)
        )
        add(num=num, k=rng.choice([1, 10**9, rng.randint(1, n * n)]))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
