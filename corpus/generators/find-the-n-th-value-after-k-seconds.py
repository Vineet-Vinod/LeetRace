def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(n=4, k=5)", "candidate(n=5, k=3)"])
    for index in range(600):
        n = 1 + index % 1000
        k = 1 + (index * 13) % 1000
        if index % 250 == 0:
            n, k = 1000, 1000
        cases.add(f"candidate(n={n}, k={k})")
    while len(cases) < 600:
        cases.add(f"candidate(n={rng.randint(1, 1000)}, k={rng.randint(1, 1000)})")
    return sorted(cases)
