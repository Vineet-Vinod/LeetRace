def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    boundary = "abcdefghijklmnopqrstuvwxyz" * 384 + "abcdefghijklmnop"
    assert len(boundary) == 10000
    cases = {
        "candidate(s='havefunonleetcode', k=5)",
        "candidate(s='home', k=5)",
        "candidate(s='a', k=1)",
        "candidate(s='aaaaa', k=1)",
        "candidate(s='abcdef', k=6)",
        "candidate(s='abcdef', k=7)",
        f"candidate(s={boundary!r}, k=1)",
        f"candidate(s={boundary!r}, k=26)",
        f"candidate(s={boundary!r}, k=27)",
        f"candidate(s={'a' * 10000!r}, k=1)",
        f"candidate(s={'a' * 10000!r}, k=10000)",
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        value = "".join(rng.choice(string.ascii_lowercase[:10]) for _ in range(size))
        k = rng.randint(1, min(size + 5, 30))
        assert 1 <= len(value) <= 10000 and 1 <= k <= 10000
        cases.add(f"candidate(s={value!r}, k={k})")
    assert len(cases) == 600
    return sorted(cases)
