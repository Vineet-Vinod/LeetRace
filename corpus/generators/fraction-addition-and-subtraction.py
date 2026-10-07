def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(expression='-1/2+1/2+1/3')", "candidate(expression='1/3-1/2')"}
    while len(cases) < 600:
        pieces = []
        for i in range(rng.randint(1, 10)):
            sign = rng.choice(["+", "-"]) if i else rng.choice(["", "-"])
            a = rng.randint(1, 10)
            b = rng.randint(1, 10)
            pieces.append(f"{sign}{a}/{b}")
        cases.add(f"candidate(expression={''.join(pieces)!r})")
    return sorted(cases)
