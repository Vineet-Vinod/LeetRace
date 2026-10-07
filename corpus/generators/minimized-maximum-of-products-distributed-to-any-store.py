import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    pairs = {(100000, (1,) * 100000), (100000, (100000,))}
    while len(pairs) < 600:
        m = rng.randint(1, 30)
        n = rng.randint(m, 60)
        quantities = tuple(rng.randint(1, 100000) for _ in range(m))
        pairs.add((n, quantities))
    cases = [
        f"candidate(n={n}, quantities={list(quantities)!r})" for n, quantities in pairs
    ]
    assert len(cases) == len(set(cases)) == 600
    assert all(
        1 <= len(q) <= n <= 100000 and all(1 <= value <= 100000 for value in q)
        for n, q in pairs
    )
    return cases
