def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        k = rng.randint(1, 100)
        rng.randint(1, 40)
        logs = [
            [rng.randint(0, 10**9), rng.randint(1, 10**5)]
            for _ in range(rng.randint(1, 100))
        ]
        k = max(k, max(len({t for u, t in logs if u == user}) for user, _ in logs))
        cases.add(f"candidate(logs={logs!r}, k={k})")
    return sorted(cases)
