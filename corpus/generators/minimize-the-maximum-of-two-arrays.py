def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        d1, d2 = rng.randint(2, 100), rng.randint(2, 100)
        c1, c2 = rng.randint(1, 100), rng.randint(1, 100)
        cases.add(
            f"candidate(divisor1={d1},divisor2={d2},uniqueCnt1={c1},uniqueCnt2={c2})"
        )
    return sorted(cases)
