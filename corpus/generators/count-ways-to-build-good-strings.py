def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(low=3, high=3, zero=1, one=1)",
            "candidate(low=2, high=3, zero=1, one=2)",
            "candidate(low=100000, high=100000, zero=1, one=1)",
        ]
    )
    for index in range(600):
        high = 1 + index % 200
        low = rng.randint(1, high)
        zero, one = rng.randint(1, low), rng.randint(1, low)
        cases.add(f"candidate(low={low}, high={high}, zero={zero}, one={one})")
    while len(cases) < 600:
        high = rng.randint(1, 500)
        low = rng.randint(1, high)
        cases.add(
            f"candidate(low={low}, high={high}, zero={rng.randint(1, low)}, one={rng.randint(1, low)})"
        )
    return sorted(cases)
