def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(plants=[2,2,3,3],capacity=5)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        plants = [rng.randint(1, 100) for _ in range(n)]
        capacity = rng.randint(max(plants), 200)
        cases.add(f"candidate(plants={plants!r},capacity={capacity})")
    return sorted(cases)
