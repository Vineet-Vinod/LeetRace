def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        a = "".join(
            rng.choice(string.ascii_lowercase[:6]) for _ in range(rng.randint(1, 30))
        )
        if rng.random() < 0.7:
            offset = rng.randrange(len(a))
            repeated = a * rng.randint(1, 10)
            b = repeated[offset : offset + rng.randint(1, 100)]
            if not b:
                b = a
        else:
            b = "".join(
                rng.choice(string.ascii_lowercase[6:12])
                for _ in range(rng.randint(1, 100))
            )
        cases.add(f"candidate(a={a!r}, b={b!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(a='a', b={'a' * 10000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
