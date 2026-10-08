def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(digits='')"}
    while len(cases) < 600:
        digits = "".join(rng.choice("23456789") for _ in range(rng.randint(1, 4)))
        cases.add(f"candidate(digits={digits!r})")
    return sorted(cases)
