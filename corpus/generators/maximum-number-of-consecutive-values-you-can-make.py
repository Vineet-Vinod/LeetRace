def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(coins=[1, 3])",
        "candidate(coins=[1, 1, 1, 4])",
        "candidate(coins=[1, 1, 3, 4])",
        "candidate(coins=[2, 3, 4])",
        f"candidate(coins={[1] * 40000!r})",
        f"candidate(coins={[1, 2] * 20000!r})",
        f"candidate(coins={list(range(1, 20001))!r})",
    }
    while len(cases) < 350:
        size = rng.randint(1, 100)
        coins = list(range(1, size + 1))
        if rng.random() < 0.5:
            coins.extend(
                rng.randint(size + 1, 40000) for _ in range(rng.randint(1, 10))
            )
        rng.shuffle(coins)
        assert 1 <= len(coins) <= 40000 and all(1 <= coin <= 40000 for coin in coins)
        cases.add(f"candidate(coins={coins!r})")

    while len(cases) < 600:
        coins = [rng.randint(1, 40000) for _ in range(rng.randint(1, 100))]
        assert 1 <= len(coins) <= 40000 and all(1 <= coin <= 40000 for coin in coins)
        cases.add(f"candidate(coins={coins!r})")
    assert len(cases) == 600
    return sorted(cases)
