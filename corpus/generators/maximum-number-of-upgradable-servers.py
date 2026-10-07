import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 60)
        count = [rng.randint(1, 100000) for _ in range(n)]
        upgrade = [rng.randint(1, 100000) for _ in range(n)]
        sell = [rng.randint(1, 100000) for _ in range(n)]
        money = [rng.randint(1, 100000) for _ in range(n)]
        key = tuple(map(tuple, (count, upgrade, sell, money)))
        if key not in seen:
            seen.add(key)
            assert all(
                len(row) == n and all(1 <= v <= 100000 for v in row)
                for row in (count, upgrade, sell, money)
            )
            cases.append(
                f"candidate(count={count!r}, upgrade={upgrade!r}, sell={sell!r}, money={money!r})"
            )
    return cases
