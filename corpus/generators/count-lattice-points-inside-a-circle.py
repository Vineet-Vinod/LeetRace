def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 10)
        circles = []
        for _ in range(n):
            x, y = rng.randint(1, 100), rng.randint(1, 100)
            r = rng.randint(1, min(x, y))
            circles.append([x, y, r])
        cases.add(f"candidate(circles={circles!r})")
    return sorted(cases)
