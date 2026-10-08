def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    names = string.ascii_lowercase[:8]
    cities = string.ascii_lowercase[8:16]
    cases = set()
    for _ in range(600):
        transactions = []
        for _ in range(rng.randint(1, 40)):
            name = "".join(rng.choice(names) for _ in range(rng.randint(1, 6)))
            city = "".join(rng.choice(cities) for _ in range(rng.randint(1, 6)))
            time = rng.randint(0, 1000)
            amount = rng.randint(0, 2000)
            transactions.append(f"{name},{time},{amount},{city}")
        cases.add(f"candidate(transactions={transactions!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(transactions={['a,0,1000,x'] * 1000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
