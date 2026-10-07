def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        days = sorted(rng.sample(range(1, 10**9), n))
        prices = [[day, rng.randint(1, 10**9)] for day in days]
        cases.add(f"candidate(stockPrices={prices!r})")
    return sorted(cases)
