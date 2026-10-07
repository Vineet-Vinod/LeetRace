def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        answers = [rng.randint(0, 999) for _ in range(rng.randint(1, 1000))]
        cases.add(f"candidate(answers={answers!r})")
    return sorted(cases)
