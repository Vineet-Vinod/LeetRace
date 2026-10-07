def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(2, 100)
        seats = [rng.randint(0, 1) for _ in range(size)]
        if all(seats):
            seats[rng.randrange(size)] = 0
        if not any(seats):
            seats[rng.randrange(size)] = 1
        assert 0 in seats and 1 in seats
        cases.add(f"candidate(seats={seats!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(seats={[1] + [0] * 19998 + [1]!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
