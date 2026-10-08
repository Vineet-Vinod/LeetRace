def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    alphabet = string.ascii_lowercase[:8]
    for _ in range(600):
        source = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 30)))
        if rng.random() < 0.7:
            target = "".join(rng.choice(source) for _ in range(rng.randint(1, 50)))
        else:
            target = "".join(
                rng.choice(string.ascii_lowercase[8:16])
                for _ in range(rng.randint(1, 50))
            )
        cases.add(f"candidate(source={source!r}, target={target!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(source={'a' * 1000!r}, target={'a' * 1000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
