import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        n, p = kwargs["n"], kwargs["paths"]
        assert 1 <= n <= 100000 and 2 <= len(p) <= 100000
        assert sum(map(len, p)) <= 100000
        assert all(
            all(0 <= x < n for x in path)
            and all(a != b for a, b in zip(path, path[1:]))
            for path in p
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=5, paths=[[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]])
    add(n=3, paths=[[0], [1], [2]])
    add(n=5, paths=[[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]])
    add(n=100000, paths=[list(range(50000)), list(range(50000))])
    add(n=1, paths=[[0] for _ in range(100000)])
    add(n=1, paths=[[0], [0]])
    add(n=100000, paths=[[99999], [99999]])
    while len(calls) < 600:
        n = rng.randint(2, 12)
        m = rng.randint(2, 6)

        def path(length):
            result = [rng.randrange(n)]
            for _ in range(length - 1):
                x = rng.randrange(n - 1)
                if x >= result[-1]:
                    x += 1
                result.append(x)
            return result

        p = [path(rng.randint(1, 22)) for _ in range(m)]
        if len(calls) % 3 == 0:
            common = path(rng.randint(1, 10))
            p = [common.copy() for _ in range(m)]
        add(n=n, paths=p)
    return calls
