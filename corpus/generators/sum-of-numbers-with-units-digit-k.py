def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {f"candidate(num={num}, k={k})" for num in range(0, 50) for k in range(10)}
    while len(cases) < 600:
        num, k = rng.randint(0, 3000), rng.randint(0, 9)
        cases.add(f"candidate(num={num}, k={k})")
    return sorted(cases)
