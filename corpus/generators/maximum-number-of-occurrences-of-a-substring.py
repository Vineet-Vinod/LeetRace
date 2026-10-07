def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        s = "".join(
            rng.choice(string.ascii_lowercase[:8]) for _ in range(rng.randint(1, 100))
        )
        minimum = rng.randint(1, min(10, len(s)))
        maximum = rng.randint(minimum, min(26, len(s)))
        max_letters = rng.randint(1, 26)
        cases.add(
            f"candidate(s={s!r}, maxLetters={max_letters}, minSize={minimum}, maxSize={maximum})"
        )
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'a' * 100000!r}, maxLetters=1, minSize=1, maxSize=26)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
