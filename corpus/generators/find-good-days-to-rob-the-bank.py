import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((5, 3, 3, 3, 5, 6, 2), 2),
        ((1, 1, 1, 1, 1), 0),
        ((1, 2, 3, 4, 5, 6), 2),
        ((5,) * 100000, 1),
        ((5,) * 100000, 100000),
        ((5,) * 100000, 0),
    }
    positive_count = 0
    while positive_count < 300:
        time = rng.randint(1, 50)
        plateau = rng.randint(1, 60)
        base = rng.randint(0, 100000 - time)
        security = tuple(
            [base + offset for offset in range(time, 0, -1)]
            + [base] * plateau
            + [base + offset for offset in range(1, time + 1)]
        )
        before = len(cases)
        cases.add((security, time))
        if len(cases) > before:
            positive_count += 1
    while len(cases) < 600:
        n = rng.randint(1, 100)
        base = rng.randint(0, 100000 - n)
        security = tuple(base + i for i in range(n))
        time = rng.randint(1, min(100000, n))
        cases.add((security, time))
    calls = [
        f"candidate(security={list(security)!r}, time={time})"
        for security, time in cases
    ]
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    assert all(
        1 <= len(security) <= 100000
        and 0 <= time <= 100000
        and all(0 <= x <= 100000 for x in security)
        for security, time in cases
    )
    return calls
