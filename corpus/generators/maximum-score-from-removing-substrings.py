def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        s = "".join(
            rng.choice(string.ascii_lowercase[:6]) for _ in range(rng.randint(1, 100))
        )
        x, y = rng.randint(1, 10000), rng.randint(1, 10000)
        cases.add(f"candidate(s={s!r}, x={x}, y={y})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'ab' * 50000!r}, x=10000, y=9999)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
