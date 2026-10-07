def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(initial='a',target='a')"}
    while len(cases) < 600:
        a = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 80)))
        b = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 80)))
        cases.add(f"candidate(initial={a!r},target={b!r})")
    return sorted(cases)
