def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ["candidate(chalk=[5, 1, 5], k=22)", "candidate(chalk=[3, 4, 1, 2], k=25)"]
    )
    for index in range(600):
        size = 1 + index % 1000
        chalk = [rng.randint(1, 100000) for _ in range(size)]
        k = rng.randint(1, 10**9)
        cases.add(f"candidate(chalk={chalk!r}, k={k})")
    while len(cases) < 600:
        chalk = [rng.randint(1, 100000) for _ in range(rng.randint(1, 100))]
        cases.add(f"candidate(chalk={chalk!r}, k={rng.randint(1, 10**9)})")
    return sorted(cases)
