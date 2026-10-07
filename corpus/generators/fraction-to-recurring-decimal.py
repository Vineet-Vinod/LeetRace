def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(numerator=1, denominator=2)",
            "candidate(numerator=4, denominator=333)",
        ]
    )
    for index in range(600):
        numerator = rng.randint(-(2**31), 2**31 - 1)
        denominator = rng.choice([-1, 1]) * rng.randint(1, 9000)
        cases.add(f"candidate(numerator={numerator}, denominator={denominator})")
    while len(cases) < 600:
        numerator = rng.randint(-100000, 100000)
        denominator = rng.choice([-1, 1]) * rng.randint(1, 9000)
        cases.add(f"candidate(numerator={numerator}, denominator={denominator})")
    return sorted(cases)
