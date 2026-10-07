def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[0])",
        "candidate(nums=[1])",
        "candidate(nums=[0, 0, 1, 0])",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(0, 1) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
