def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='001101')"}
    while len(cases) < 600:
        n = rng.randint(3, 200)
        s = "".join(rng.choice("01") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
