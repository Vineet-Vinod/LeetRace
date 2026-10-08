def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        s = "".join(rng.choice("ID") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
