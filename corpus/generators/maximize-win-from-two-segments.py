def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(prizePositions=[1, 1, 2, 2, 3, 3, 5], k=2)"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 200
        positions = sorted(rng.randint(1, 10**9) for _ in range(size))
        k = rng.randint(0, 10**9)
        cases.add(f"candidate(prizePositions={positions!r}, k={k})")
    return sorted(cases)
