def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        kinds = rng.randint(1, 40)
        counts = [rng.randint(1, 100000) for _ in range(kinds)]
        queries = [
            [rng.randrange(kinds), rng.randint(0, 10**9), rng.randint(1, 10**9)]
            for _ in range(rng.randint(1, 30))
        ]
        assert all(0 <= q[0] < kinds and q[1] >= 0 and q[2] > 0 for q in queries)
        cases.add(f"candidate(candiesCount={counts!r}, queries={queries!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(candiesCount={[1] * 100000!r}, queries={[[0, 0, 1000000000], [99999, 99999, 1]] * 50000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
