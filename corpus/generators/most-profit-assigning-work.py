def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n, m = rng.randint(1, 100), rng.randint(1, 100)
        difficulty = [rng.randint(1, 10**5) for _ in range(n)]
        profit = [rng.randint(1, 10**5) for _ in range(n)]
        worker = [rng.randint(1, 10**5) for _ in range(m)]
        cases.add(
            f"candidate(difficulty={difficulty!r}, profit={profit!r}, worker={worker!r})"
        )
    return sorted(cases)
