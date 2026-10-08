import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        k = rng.randint(1, 1 << (n - 1))
        key = (n, k)
        if key not in seen:
            seen.add(key)
            assert 1 <= n <= 30 and 1 <= k <= 1 << (n - 1)
            cases.append(f"candidate(n={n}, k={k})")
    return cases
