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
        a = k["nums1"]
        b = k["nums2"]
        assert (
            1 <= len(a) <= 100000
            and len(a) == len(b)
            and all(1 <= x <= 10000 for x in a + b)
        )

    add(nums1=[60, 60, 60], nums2=[10, 90, 10])
    add(nums1=[20, 40, 20, 70, 30], nums2=[50, 20, 50, 40, 20])
    add(nums1=[7, 11, 13], nums2=[1, 1, 1])
    add(nums1=[10000] * 100000, nums2=[1] * 100000)
    add(nums1=[1, 10000] * 50000, nums2=[10000, 1] * 50000)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        a = [rng.randint(1, 100) for _ in range(n)]
        b = a[:] if len(calls) % 5 == 0 else [rng.randint(1, 100) for _ in range(n)]
        add(nums1=a, nums2=b)
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
