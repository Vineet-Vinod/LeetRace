def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(['candidate(s="a1b2")', 'candidate(s="3z4")'])
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for index in range(600):
        size = 1 + index % 12
        s = "".join(rng.choice(alphabet) for _ in range(size))
        cases.add(f"candidate(s={s!r})")
    while len(cases) < 600:
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 12)))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
