def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        s = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
        )
        t = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
        )
        cases.add(f"candidate(s={s!r}, t={t!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'a' * 100000!r}, t={'a' * 100000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
