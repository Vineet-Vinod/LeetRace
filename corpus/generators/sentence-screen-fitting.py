def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        sentence = [
            "".join(
                rng.choice(string.ascii_lowercase[:8])
                for _ in range(rng.randint(1, 10))
            )
            for _ in range(rng.randint(1, 20))
        ]
        rows, cols = rng.randint(1, 100), rng.randint(1, 100)
        cases.add(f"candidate(sentence={sentence!r}, rows={rows}, cols={cols})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(sentence={['a'] * 100!r}, rows=20000, cols=20000)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
