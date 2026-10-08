def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='deeedbbcccbdaa',k=3)"}
    while len(cases) < 600:
        n = rng.randint(1, 500)
        s = "".join(rng.choice("abcdef") for _ in range(n))
        k = rng.randint(2, 100)
        cases.add(f"candidate(s={s!r},k={k})")
    return sorted(cases)
