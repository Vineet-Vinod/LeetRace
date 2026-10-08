def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = {"candidate(word='asdf')", "candidate(word='bdh')"}
    while len(cases) < 600:
        word = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 80))
        )
        cases.add(f"candidate(word={word!r})")
    return sorted(cases)
