import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        queries = []
        for _ in range(rng.randint(1, 40)):
            r1 = rng.randrange(n)
            r2 = rng.randint(r1, n - 1)
            c1 = rng.randrange(n)
            c2 = rng.randint(c1, n - 1)
            queries.append([r1, c1, r2, c2])
        key = (n, tuple(map(tuple, queries)))
        if key not in seen:
            seen.add(key)
            assert all(
                0 <= r1 <= r2 < n and 0 <= c1 <= c2 < n for r1, c1, r2, c2 in queries
            )
            cases.append(f"candidate(n={n}, queries={queries!r})")
    return cases
