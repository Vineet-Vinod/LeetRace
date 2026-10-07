def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {f"candidate(n={n})" for n in range(1, 101)}
    while len(cases) < 600:
        cases.add(f"candidate(n={rng.randint(1, 1690)})")
    return sorted(cases)
