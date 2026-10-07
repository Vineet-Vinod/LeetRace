def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(n=6,delay=2,forget=4)"}
    while len(cases) < 600:
        n = rng.randint(2, 1000)
        delay = rng.randint(1, n - 1)
        forget = rng.randint(delay + 1, n)
        cases.add(f"candidate(n={n},delay={delay},forget={forget})")
    return sorted(cases)
