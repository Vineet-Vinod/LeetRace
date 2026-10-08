def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        count = [0] * 256
        mode = rng.randrange(256)
        count[mode] = 1000
        for _ in range(rng.randint(1, 20)):
            value = rng.randrange(256)
            if value != mode:
                count[value] = rng.randint(1, 100)
        assert 1 <= sum(count) <= 10**9
        assert count[mode] > max(
            (amount for value, amount in enumerate(count) if value != mode), default=0
        )
        cases.add(f"candidate(count={count!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
