def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(0, 100) for _ in range(n)]
        queries = [[rng.randint(0, 10**5), rng.randrange(n)] for _ in range(n)]
        cases.add(f"candidate(nums={nums!r}, queries={queries!r})")
    return sorted(cases)
