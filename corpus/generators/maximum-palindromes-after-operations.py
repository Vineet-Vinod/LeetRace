def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(words=['abbb','ba','aa'])"}
    while len(cases) < 600:
        n = rng.randint(1, 30)
        words = [
            "".join(rng.choice("abcdef") for _ in range(rng.randint(1, 30)))
            for _ in range(n)
        ]
        cases.add(f"candidate(words={words!r})")
    return sorted(cases)
