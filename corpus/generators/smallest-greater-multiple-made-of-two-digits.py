def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(k=2, digit1=0, digit2=2)",
        "candidate(k=3, digit1=4, digit2=2)",
        "candidate(k=2, digit1=0, digit2=0)",
        "candidate(k=1, digit1=9, digit2=9)",
    }
    while len(cases) < 600:
        k = rng.randint(1, 1000)
        a, b = rng.randint(0, 9), rng.randint(0, 9)
        assert 1 <= k <= 1000 and 0 <= a <= 9 and 0 <= b <= 9
        cases.add(f"candidate(k={k}, digit1={a}, digit2={b})")
    return sorted(cases)
