def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        limit = rng.randint(1, 100)
        nums = [rng.randint(1, limit) for _ in range(2 * rng.randint(1, 50))]
        cases.add(f"candidate(nums={nums!r}, limit={limit})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={[1, 100000] * 50000!r}, limit=100000)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
