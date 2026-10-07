def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    cases.update(("candidate(s='0')", "candidate(s='1')", "candidate(s='00011')"))
    for _ in range(597):
        size = rng.randint(1, 100)
        s = "".join(rng.choice("01") for _ in range(size))
        cases.add(f"candidate(s={s!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'1' * 40000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
