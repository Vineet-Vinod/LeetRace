import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        n, e = kwargs["n"], kwargs["edges"]
        assert 2 <= n <= 15 and len(e) == n - 1
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for a, b in e:
            assert 1 <= a <= n and 1 <= b <= n and find(a) != find(b)
            parent[find(a)] = find(b)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=4, edges=[[1, 2], [2, 3], [2, 4]])
    add(n=2, edges=[[1, 2]])
    add(n=3, edges=[[1, 2], [2, 3]])
    add(n=15, edges=[[i, i + 1] for i in range(1, 15)])
    add(n=15, edges=[[1, i] for i in range(2, 16)])
    while len(calls) < 600:
        n = rng.randint(3, 9)
        e = [[i, rng.randrange(1, i)] for i in range(2, n + 1)]
        rng.shuffle(e)
        add(n=n, edges=e)
    return calls
