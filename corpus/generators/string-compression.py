def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    cases = set()
    for _ in range(600):
        chars = [rng.choice(alphabet) for _ in range(rng.randint(1, 2000))]
        if rng.random() < 0.8:
            start = rng.randrange(len(chars))
            end = min(len(chars), start + rng.randint(2, 100))
            chars[start:end] = [chars[start]] * (end - start)
        cases.add(
            f"(lambda chars: (lambda length: (length, chars[:length]))(candidate(chars)) )({chars!r})"
        )
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"(lambda chars: (lambda length: (length, chars[:length]))(candidate(chars)) )({['a'] * 2000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
