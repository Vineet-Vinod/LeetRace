def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(startValue=2, target=3)",
        "candidate(startValue=5, target=8)",
        "candidate(startValue=3, target=10)",
    }
    while len(cases) < 600:
        start, target = rng.randint(1, 10**9), rng.randint(1, 10**9)
        cases.add(f"candidate(startValue={start}, target={target})")
    return sorted(cases)
