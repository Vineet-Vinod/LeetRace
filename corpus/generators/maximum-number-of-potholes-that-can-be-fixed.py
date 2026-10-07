def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(road='..xxxxx',budget=4)",
        f"candidate(road={'x' * 5000!r},budget=5001)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 300)
        road = "".join(rng.choice("x.") for _ in range(n))
        budget = rng.randint(1, n + 1)
        cases.add(f"candidate(road={road!r},budget={budget})")
    return sorted(cases)
