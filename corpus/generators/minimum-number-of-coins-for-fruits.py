def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(prices=[3,1,2])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        prices = [rng.randint(1, 1000) for _ in range(n)]
        cases.add(f"candidate(prices={prices!r})")
    return sorted(cases)
