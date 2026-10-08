import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 2, 7), 80),
        ((2, 3, 6), 50),
        ((3, 3, 3, 3), 40),
        ((0,), 0),
        ((0, 100_000), 99),
        ((100_000,) * 100_000, 99),
    }
    while len(cases) < 600:
        buckets = tuple(rng.randint(0, 100_000) for _ in range(rng.randint(1, 50)))
        cases.add((buckets, rng.randint(0, 99)))
    assert all(
        1 <= len(buckets) <= 100_000
        and all(0 <= amount <= 100_000 for amount in buckets)
        and 0 <= loss <= 99
        for buckets, loss in cases
    )
    return [
        f"candidate(buckets={list(buckets)!r}, loss={loss})"
        for buckets, loss in sorted(cases)
    ]
