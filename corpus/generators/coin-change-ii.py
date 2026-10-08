import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, tuple[int, ...]]] = {
        (0, (1,)),
        (5, (1, 2, 5)),
        (3, (2,)),
        (10, (10,)),
        (5000, (1, 4999, 5000)),
        (100, (1, 2, 3, 4, 5)),
        (100, tuple(range(1, 301))),
    }
    while len(cases) < 600:
        amount = rng.randint(0, 500)
        count = rng.randint(1, 18)
        coins = tuple(sorted(rng.sample(range(1, 501), count)))
        cases.add((amount, coins))
    assert all(
        0 <= amount <= 5000
        and 1 <= len(coins) <= 300
        and len(set(coins)) == len(coins)
        and all(1 <= coin <= 5000 for coin in coins)
        for amount, coins in cases
    )
    return [
        f"candidate(amount={amount}, coins={list(coins)!r})"
        for amount, coins in sorted(cases)
    ]
