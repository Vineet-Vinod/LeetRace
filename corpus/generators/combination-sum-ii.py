def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        candidates = [rng.randint(1, 50) for _ in range(rng.randint(1, 30))]
        target = rng.randint(1, 30)
        assert all(1 <= value <= 50 for value in candidates)
        cases.add(f"candidate(candidates={candidates!r}, target={target})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(candidates={[1] * 100!r}, target=30)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
