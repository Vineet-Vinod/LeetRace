def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='tree')"}
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while len(cases) < 600:
        n = rng.randint(1, 500)
        s = "".join(rng.choice(alphabet) for _ in range(n))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
