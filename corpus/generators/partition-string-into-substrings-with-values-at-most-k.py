def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='165462',k=60)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        s = "".join(rng.choice("123456789") for _ in range(n))
        k = rng.randint(1, 10**9)
        cases.add(f"candidate(s={s!r},k={k})")
    return sorted(cases)
