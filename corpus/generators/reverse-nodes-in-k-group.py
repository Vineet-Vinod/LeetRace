import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        validate(kw)
        collect = "list(iter(lambda state=[VALUE]: (lambda node: (state.__setitem__(0,node.next),node)[1] if node else None)(state[0]),None))"
        returned = collect.replace("VALUE", "result")
        original = collect.replace("VALUE", "head")
        call = (
            "(lambda head: (lambda nodes: (lambda indices: (lambda result: "
            "(repr(result), repr(head), [(indices.get(id(node),-1),node.val) for node in "
            + returned
            + "]))"
            "(candidate(head, " + repr(kw["k"]) + ")))"
            "({id(node): i for i,node in enumerate(nodes)}))(" + original + "))"
            "(list_node(" + repr(kw["head"]) + "))"
        )
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
        assert 1 <= k["k"] <= len(k["head"]) <= 5000 and all(
            0 <= x <= 1000 for x in k["head"]
        )

    add(head=[1, 2, 3, 4, 5], k=2)
    add(head=[1, 2, 3, 4, 5], k=3)
    add(head=[i % 1001 for i in range(5000)], k=5000)
    add(head=[i % 1001 for i in range(5000)], k=2)
    while len(calls) < 600:
        n = rng.randint(1, 90)
        add(head=[rng.randint(0, 1000) for _ in range(n)], k=rng.randint(1, n))
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
