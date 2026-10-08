def generate(seed: int = 0) -> list[str]:
    import random
    import math

    rng = random.Random(seed)
    cases = {
        "candidate(m=3, n=7)",
        "candidate(m=3, n=2)",
        "candidate(m=1, n=100)",
        "candidate(m=100, n=1)",
        "candidate(m=17, n=17)",
    }
    while len(cases) < 600:
        m, n = rng.randint(1, 100), rng.randint(1, 100)
        if math.comb(m + n - 2, m - 1) <= 2 * 10**9:
            cases.add(f"candidate(m={m}, n={n})")
    return sorted(cases)
