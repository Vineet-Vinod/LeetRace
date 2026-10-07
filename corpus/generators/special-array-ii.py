def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 200)
        nums = [rng.randint(1, 10**5) for _ in range(n)]
        queries = []
        for _ in range(rng.randint(1, 100)):
            left_index = rng.randrange(n)
            queries.append([left_index, rng.randint(left_index, n - 1)])
        cases.add(f"candidate(nums={nums!r}, queries={queries!r})")
    return sorted(cases)
