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
        p = k["parent"]
        s = k["s"]
        n = len(p)
        assert 1 <= n <= 10**5 and len(s) == n and lower(s) and p[0] == -1
        valid_tree(n, [[i, p[i]] for i in range(1, n)])

    add(parent=[-1, 0, 0, 1, 1, 2], s="acaabc")
    add(parent=[-1, 0, 0, 0, 0], s="aaaaa")
    add(parent=[-1] + list(range(99999)), s="a" * 100000)
    add(parent=[-1] + [0] * 99999, s=("abcdefghijklmnopqrstuvwxyz" * 3847)[:100000])
    while len(calls) < 600:
        n = rng.randint(1, 80)
        edges = tree(n, len(calls) % 3)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        p = [-1] * n
        order = [0]
        for a in order:
            for b in graph[a]:
                if b != p[a]:
                    p[b] = a
                    order.append(b)
        add(
            parent=p,
            s=letters(
                n, rng.choice(["a", "ab", "abcdef", "abcdefghijklmnopqrstuvwxyz"])
            ),
        )
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
