def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        s = "".join(rng.choice("abc") for _ in range(rng.randint(1, 100)))
        k = rng.randint(0, len(s))
        cases.add(f"candidate(s={s!r}, k={k})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'abc' * 33333 + 'a'!r}, k=1000)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
