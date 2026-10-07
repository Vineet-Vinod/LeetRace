import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    pairs = {(1, 1), (1, 2), (3, 2), (100_000, 100_000), (1, 100_000)}
    while len(pairs) < 600:
        pairs.add((rng.randint(1, 100_000), rng.randint(1, 100_000)))
    assert all(1 <= n <= 100_000 and 1 <= m <= 100_000 for n, m in pairs)
    return [f"candidate(n={n}, m={m})" for n, m in sorted(pairs)]
