def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {(1, 1), (3, 4), (2, 7), (10**8, 10**8)}
    while len(cases) < 600:
        cases.add((rng.randint(1, 10**8), rng.randint(1, 10**8)))
    return [f"candidate(n={n}, x={x})" for n, x in sorted(cases)]
