import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        lists = []
        keys = set()
        while len(lists) < n:
            values = rng.sample(
                [
                    f"company{chr(97 + i // 26) if i >= 26 else ''}{chr(97 + i % 26)}"
                    for i in range(40)
                ],
                rng.randint(1, 12),
            )
            key = tuple(sorted(values))
            if key not in keys:
                keys.add(key)
                lists.append(values)
        key = tuple(tuple(sorted(row)) for row in lists)
        if key not in seen:
            seen.add(key)
            assert all(len(row) == len(set(row)) for row in lists) and len(key) == len(
                set(key)
            )
            cases.append(f"candidate(favoriteCompanies={lists!r})")
    return cases
