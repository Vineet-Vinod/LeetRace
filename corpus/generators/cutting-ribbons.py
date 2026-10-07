import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        ribbons = [rng.randint(1, 100000) for _ in range(rng.randint(1, 40))]
        k = rng.randint(1, 100)
        key = (tuple(ribbons), k)
        if key not in seen:
            seen.add(key)
            assert ribbons and all(1 <= r <= 10**5 for r in ribbons)
            cases.append(f"candidate(ribbons={ribbons!r}, k={k})")
    return cases
