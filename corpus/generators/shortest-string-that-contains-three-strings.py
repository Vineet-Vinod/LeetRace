def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(a='abc',b='bca',c='aaa')"}
    while len(cases) < 600:
        a, b, c = [
            "".join(rng.choice("abcde") for _ in range(rng.randint(1, 20)))
            for _ in range(3)
        ]
        cases.add(f"candidate(a={a!r},b={b!r},c={c!r})")
    return sorted(cases)
