def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(599):
        s = "".join(
            rng.choice(string.ascii_lowercase[:8]) for _ in range(rng.randint(1, 80))
        )
        cases.add(f"candidate(s={s!r})")
    cases.add(f"candidate(s={'a' * 500!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
