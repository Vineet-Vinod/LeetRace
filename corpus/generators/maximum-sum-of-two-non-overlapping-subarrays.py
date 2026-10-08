def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 1000)
        a = rng.randint(1, n - 1)
        b = rng.randint(1, n - a)
        nums = [rng.randint(0, 1000) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r}, firstLen={a}, secondLen={b})")
    return sorted(cases)
