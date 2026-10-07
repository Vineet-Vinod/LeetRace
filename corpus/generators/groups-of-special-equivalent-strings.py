def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(1, 40)
        word_length = rng.randint(1, 20)
        words = [
            "".join(rng.choice(string.ascii_lowercase[:8]) for _ in range(word_length))
            for _ in range(size)
        ]
        assert len({len(word) for word in words}) == 1
        cases.add(f"candidate(words={words!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(words={['abcd'] * 1000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
