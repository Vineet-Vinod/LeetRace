def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {f"candidate(n={n})" for n in [1, 2, 12, 37, 64, 100]}
    while len(cases) < 600:
        cases.add(f"candidate(n={rng.randint(1, 10**7)})")
    return sorted(cases)
