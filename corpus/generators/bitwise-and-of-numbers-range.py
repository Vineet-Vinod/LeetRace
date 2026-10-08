import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    maximum = 2**31 - 1
    pairs = {
        (0, 0),
        (0, maximum),
        (5, 7),
        (1, 2),
        (8, 15),
        (maximum - 1, maximum),
        (2**30, 2**30 + 100),
    }
    while len(pairs) < 600:
        left = rng.randint(0, maximum)
        right = min(maximum, left + rng.randint(0, 100_000))
        pairs.add((left, right))
    assert all(0 <= left <= right <= maximum for left, right in pairs)
    return [f"candidate(left={left}, right={right})" for left, right in sorted(pairs)]
