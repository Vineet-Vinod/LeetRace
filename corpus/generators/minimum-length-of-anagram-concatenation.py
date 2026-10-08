def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        base = "".join(
            rng.choice(string.ascii_lowercase[:8]) for _ in range(rng.randint(1, 20))
        )
        chunks = []
        for _ in range(rng.randint(1, 12)):
            chunk = list(base)
            rng.shuffle(chunk)
            chunks.append("".join(chunk))
        s = "".join(chunks)
        assert all(CounterLike(chunk) == CounterLike(base) for chunk in chunks)
        cases.add(f"candidate(s={s!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def CounterLike(value: str) -> tuple[tuple[str, int], ...]:
    from collections import Counter

    return tuple(sorted(Counter(value).items()))


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'abc' * 33333 + 'a'!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
