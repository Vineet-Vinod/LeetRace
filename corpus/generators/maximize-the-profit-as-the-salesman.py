def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 50)
        offers = []
        for _ in range(rng.randint(1, 80)):
            start = rng.randrange(n)
            end = rng.randrange(start, n)
            offers.append([start, end, rng.randint(1, 1000)])
        cases.add(f"candidate(n={n},offers={offers!r})")
    return sorted(cases)
