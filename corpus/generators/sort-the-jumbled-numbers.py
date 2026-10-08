def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        mapping = list(range(10))
        rng.shuffle(mapping)
        nums = [rng.randint(0, 10**9 - 1) for _ in range(rng.randint(1, 100))]
        assert sorted(mapping) == list(range(10))
        cases.add(f"candidate(mapping={mapping!r}, nums={nums!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = (
        f"candidate(mapping={list(range(9, -1, -1))!r}, nums={list(range(30000))!r})"
    )
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
