def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for n in range(1, 301):
        factors = [value for value in range(1, n + 1) if n % value == 0]
        for k in {1, len(factors), max(1, len(factors) // 2), len(factors) + 1}:
            if k <= n:
                cases.add(f"candidate(n={n}, k={k})")
    for _ in range(500):
        n = rng.randint(1, 1000)
        divisors = [value for value in range(1, n + 1) if n % value == 0]
        if rng.random() < 0.75:
            k = rng.randint(1, len(divisors))
        else:
            k = rng.randint(len(divisors) + 1, n) if len(divisors) < n else n
        cases.add(f"candidate(n={n}, k={k})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
