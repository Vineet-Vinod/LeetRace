def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    letters = string.ascii_lowercase
    cases = set()
    for _ in range(600):
        chars = "".join(rng.sample(letters, rng.randint(1, 26)))
        vals = [rng.randint(-1000, 1000) for _ in chars]
        s = "".join(rng.choice(letters) for _ in range(rng.randint(1, 100)))
        assert len(chars) == len(set(chars)) and len(chars) == len(vals)
        cases.add(f"candidate(s={s!r}, chars={chars!r}, vals={vals!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'a' * 100000!r}, chars='a', vals=[1000])"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
