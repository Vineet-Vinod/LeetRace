def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='aaa')"}
    while len(cases) < 600:
        n = rng.randint(1, 200)
        s = "".join(rng.choice("abcde") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
