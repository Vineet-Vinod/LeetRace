def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='abc')"}
    while len(cases) < 600:
        n = rng.randint(3, 500)
        s = "".join(rng.choice("abc") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
