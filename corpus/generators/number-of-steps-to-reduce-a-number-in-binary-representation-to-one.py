def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='1')", "candidate(s='1101')"}
    while len(cases) < 600:
        n = rng.randint(1, 500)
        s = "1" + "".join(rng.choice("01") for _ in range(n - 1))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
