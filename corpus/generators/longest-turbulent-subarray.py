def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(arr=[9,4,2,10,7,8,8,1,9])"}
    while len(cases) < 600:
        arr = [rng.randint(0, 10**9) for _ in range(rng.randint(1, 150))]
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
