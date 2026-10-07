def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(n=15)",
        "candidate(n=3)",
        "candidate(n=100000)",
        "candidate(n=2)",
    }
    while len(cases) < 600:
        n = rng.randint(2, 100000)
        assert 2 <= n <= 100000
        cases.add(f"candidate(n={n})")
    return sorted(cases)
