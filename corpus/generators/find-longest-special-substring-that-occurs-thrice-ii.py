def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = {"candidate(s='aaaa')", "candidate(s='abcdef')"}
    while len(cases) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase[:5]) for _ in range(rng.randint(3, 150))
        )
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
