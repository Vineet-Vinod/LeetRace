def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 10000)
        banned = rng.sample(range(1, 10001), rng.randint(1, 100))
        max_sum = rng.randint(1, 10**9)
        cases.add(f"candidate(banned={banned!r},n={n},maxSum={max_sum})")
    return sorted(cases)
