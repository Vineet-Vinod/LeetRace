def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(1, 100)
        values = sorted(rng.sample(range(1, 1000000), size))
        k = rng.randint(1, 10**8)
        assert values == sorted(set(values))
        cases.add(f"candidate(nums={values!r}, k={k})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={list(range(1, 50001))!r}, k=100000)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
