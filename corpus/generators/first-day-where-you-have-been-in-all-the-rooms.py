def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(2, 100)
        next_visit = [rng.randint(0, index) for index in range(size)]
        assert all(0 <= value <= index for index, value in enumerate(next_visit))
        cases.add(f"candidate(nextVisit={next_visit!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nextVisit={[0] * 100000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
