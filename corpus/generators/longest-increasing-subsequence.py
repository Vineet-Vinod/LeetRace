def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[10,9,2,5,3,7,101,18])", "candidate(nums=[7,7,7,7])"}
    while len(cases) < 600:
        nums = [rng.randint(-10000, 10000) for _ in range(rng.randint(1, 200))]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
