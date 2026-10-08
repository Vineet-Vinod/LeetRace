def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='bab',t='aba')"}
    while len(cases) < 600:
        n = rng.randint(1, 300)
        s = "".join(rng.choice("abcdef") for _ in range(n))
        t = "".join(rng.choice("abcdef") for _ in range(n))
        cases.add(f"candidate(s={s!r},t={t!r})")
    return sorted(cases)
