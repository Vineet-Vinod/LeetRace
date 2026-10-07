def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='a',k=0)"}
    while len(cases) < 600:
        n = rng.randint(1, 500)
        s = "".join(rng.choice("abcdefghij") for _ in range(n))
        k = rng.randint(0, 50)
        cases.add(f"candidate(s={s!r},k={k})")
    return sorted(cases)
