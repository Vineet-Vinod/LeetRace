def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = {
        "candidate(s='cbaebabacd', p='abc')",
        "candidate(s='abab', p='ab')",
        "candidate(s='aaaaa', p='a')",
        "candidate(s='abc', p='d')",
        "candidate(s='a', p='aa')",
        f"candidate(s={'a' * 30000!r}, p='a')",
        f"candidate(s={'a' * 30000!r}, p={'a' * 15000!r})",
        f"candidate(s={'a' * 30000!r}, p={'b' * 15000!r})",
        f"candidate(s={'a' * 30000!r}, p={'a' * 30000!r})",
        f"candidate(s={'a' * 30000!r}, p={'a' * 29999 + 'b'!r})",
    }

    while len(cases) < 350:
        pattern = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 15))
        )
        size = rng.randint(len(pattern), 100)
        text = [rng.choice(string.ascii_lowercase) for _ in range(size)]
        start = rng.randint(0, size - len(pattern))
        window = list(pattern)
        rng.shuffle(window)
        text[start : start + len(pattern)] = window
        value = "".join(text)
        assert 1 <= len(pattern) <= len(value) <= 30000
        cases.add(f"candidate(s={value!r}, p={pattern!r})")

    while len(cases) < 600:
        value = "".join(
            rng.choice(string.ascii_lowercase[:6]) for _ in range(rng.randint(1, 100))
        )
        pattern = "".join(
            rng.choice(string.ascii_lowercase[:6]) for _ in range(rng.randint(1, 30))
        )
        assert 1 <= len(value) <= 30000 and 1 <= len(pattern) <= 30000
        cases.add(f"candidate(s={value!r}, p={pattern!r})")
    assert len(cases) == 600
    return sorted(cases)
