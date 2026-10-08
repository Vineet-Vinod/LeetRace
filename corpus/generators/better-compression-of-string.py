def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        pairs = [
            (rng.choice(string.ascii_lowercase), rng.randint(1, 10000))
            for _ in range(rng.randint(1, 30))
        ]
        assert all(
            letter in string.ascii_lowercase and 1 <= count <= 10000
            for letter, count in pairs
        )
        compressed = "".join(letter + str(count) for letter, count in pairs)
        cases.add(f"candidate(compressed={compressed!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(compressed={'a1' * 30000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
