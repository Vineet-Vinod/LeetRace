def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        a = "".join(rng.choice(string.ascii_lowercase[:6]) for _ in range(n))
        b = list(a)
        for i in range(n):
            if rng.random() < 0.2:
                b[i] = rng.choice(string.ascii_lowercase[:6])
        cases.add(f"candidate(s1={a!r}, s2={''.join(b)!r})")
    return sorted(cases)
