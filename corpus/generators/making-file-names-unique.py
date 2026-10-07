def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        names = [
            "".join(
                rng.choice(string.ascii_lowercase[:8]) for _ in range(rng.randint(1, 8))
            )
            for _ in range(rng.randint(1, 80))
        ]
        cases.add(f"candidate(names={names!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(names={['duplicate'] * 50000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
