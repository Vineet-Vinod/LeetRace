def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='a')", "candidate(s='aabcbbca')", "candidate(s='abcd')"}
    while len(cases) < 600:
        n = rng.randint(1, 150)
        s = "".join(rng.choice("abcdef") for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
