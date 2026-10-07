import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(3, 100)
        prices = [rng.randint(1, 10**6) for _ in range(n)]
        profits = [rng.randint(1, 10**6) for _ in range(n)]
        key = (tuple(prices), tuple(profits))
        if key not in seen:
            seen.add(key)
            assert len(prices) == len(profits) >= 3 and all(
                1 <= v <= 10**6 for v in prices + profits
            )
            cases.append(f"candidate(prices={prices!r}, profits={profits!r})")
    return cases
