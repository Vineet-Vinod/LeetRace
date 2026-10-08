def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = {
        "candidate(s1='ab', s2='eidbaooo')",
        "candidate(s1='ab', s2='eidboaoo')",
        f"candidate(s1={'a' * 10000!r}, s2={'a' * 10000!r})",
    }
    while len(cases) < 600:
        size = rng.randint(1, 1000)
        pattern_size = rng.randint(1, size)
        s1 = "".join(rng.choice(string.ascii_lowercase) for _ in range(pattern_size))
        s2 = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        if rng.random() < 0.5:
            start = rng.randrange(size - pattern_size + 1)
            permutation = "".join(rng.sample(list(s1), len(s1)))
            s2 = s2[:start] + permutation + s2[start + pattern_size :]
        assert 1 <= len(s1) <= 10_000 and 1 <= len(s2) <= 10_000
        cases.add(f"candidate(s1={s1!r}, s2={s2!r})")
    return sorted(cases)
