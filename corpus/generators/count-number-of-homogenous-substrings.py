def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='a')"}
    while len(cases) < 600:
        n = rng.randint(1, 200)
        s = "".join(rng.choice("abcdef") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
