def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        limit = rng.randint(1, 30000)
        size = rng.randint(1, 90)
        people = [rng.randint(1, limit) for _ in range(size)]
        assert all(1 <= weight <= limit for weight in people)
        cases.add(f"candidate(people={people!r}, limit={limit})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(people={[15000] * 50000!r}, limit=30000)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
