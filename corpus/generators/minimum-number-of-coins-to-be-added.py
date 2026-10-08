import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 4, 10), 19),
        ((1, 1, 1), 20),
        ((1,), 1),
        ((10,), 10),
    }
    cases.add((tuple(range(1, 100_001)), 100_000))
    while len(cases) < 600:
        target = rng.randint(1, 100_000)
        coins = tuple(rng.randint(1, target) for _ in range(rng.randint(1, 50)))
        cases.add((coins, target))
    assert all(
        1 <= target <= 100_000
        and 1 <= len(coins) <= 100_000
        and all(1 <= coin <= target for coin in coins)
        for coins, target in cases
    )
    return [
        f"candidate(coins={list(coins)!r}, target={target})"
        for coins, target in sorted(cases)
    ]
