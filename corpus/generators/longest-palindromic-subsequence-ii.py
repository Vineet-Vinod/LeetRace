def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(s='aa')",
        "candidate(s='bbabab')",
        f"candidate(s={'abcd' * 62 + 'ab'!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 80)
        s = "".join(rng.choice("abcd") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
