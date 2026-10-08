def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    false_cases = {
        "candidate(s='b')",
        "candidate(s='bbcd')",
        f"candidate(s={'b' * 100000!r})",
    }
    true_cases = {
        "candidate(s='a')",
        "candidate(s='leetcoder')",
        f"candidate(s={'a' * 100000!r})",
        f"candidate(s={('b' * 49999 + 'e' + 'b' * 50000)!r})",
        f"candidate(s={('aeiou' * 20000)!r})",
    }
    while len(false_cases) < 300:
        value = "".join(rng.choice(consonants) for _ in range(rng.randint(1, 100)))
        assert 1 <= len(value) <= 100000 and all(char in consonants for char in value)
        false_cases.add(f"candidate(s={value!r})")
    while len(true_cases) < 300:
        value = rng.choice(vowels) + "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(0, 99))
        )
        assert 1 <= len(value) <= 100000 and any(char in vowels for char in value)
        true_cases.add(f"candidate(s={value!r})")
    cases = false_cases | true_cases
    assert len(cases) == 600
    return sorted(cases)
