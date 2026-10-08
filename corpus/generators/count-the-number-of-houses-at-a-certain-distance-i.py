import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        n = rng.randint(2, 100)
        x = rng.randint(1, n)
        y = rng.randint(1, n)
        key = (n, x, y)
        if key not in seen:
            seen.add(key)
            assert 2 <= n <= 100 and 1 <= x <= n and 1 <= y <= n
            cases.append(f"candidate(n={n}, x={x}, y={y})")
    return cases
