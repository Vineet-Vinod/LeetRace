import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 1, 1), (1, 2, 1), (3, 3, 2), (200, 200, 200), (200, 1, 1)}
    while len(cases) < 600:
        zero = rng.randint(1, 30)
        one = rng.randint(1, 30)
        limit = rng.randint(1, max(zero, one))
        cases.add((zero, one, limit))
    assert all(
        1 <= zero <= 200 and 1 <= one <= 200 and 1 <= limit <= 200
        for zero, one, limit in cases
    )
    return [
        f"candidate(zero={zero}, one={one}, limit={limit})"
        for zero, one, limit in sorted(cases)
    ]
