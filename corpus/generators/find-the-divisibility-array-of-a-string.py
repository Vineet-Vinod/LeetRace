def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        word = "".join(rng.choice("0123456789") for _ in range(n))
        m = rng.randint(1, 10**9)
        cases.add(f"candidate(word={word!r},m={m})")
    return sorted(cases)
