def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(arr=[0])", "candidate(arr=[1,1,2])", "candidate(arr=[1,2,4])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        arr = [rng.randint(0, 10**9) for _ in range(n)]
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
