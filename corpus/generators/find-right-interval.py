def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(intervals=[[1,2]])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        starts = rng.sample(range(-(10**6), 10**6 + 1), n)
        intervals = [[x, rng.randint(x, 10**6)] for x in starts]
        cases.add(f"candidate(intervals={intervals!r})")
    return sorted(cases)
