def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        a = [rng.randint(-1000, 1000) for _ in range(n)]
        lo = rng.randint(-2000, 1000)
        hi = rng.randint(lo, 2000)
        cases.add(f"candidate(nums={a!r},lower={lo},upper={hi})")
    return sorted(cases)
