import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((1, 4, 6), 6, 4),
        ((4, 3, 5, 6), 7, 18),
        ((10**9,), 10**9, 10**15),
        ((1, 2, 3, 4), 4, 1),
    }
    cases.add((tuple(range(1, 100_001)), 10**9, 10**15))
    while len(cases) < 600:
        n = rng.randint(1, 10_000)
        banned = tuple(sorted(rng.sample(range(1, n + 1), rng.randint(1, min(n, 80)))))
        cases.add((banned, n, rng.randint(1, 10**7)))
    assert all(
        1 <= n <= 10**9
        and len(banned) <= 100_000
        and len(set(banned)) == len(banned)
        and all(1 <= value <= n for value in banned)
        and 1 <= max_sum <= 10**15
        for banned, n, max_sum in cases
    )
    return [
        f"candidate(banned={list(banned)!r}, n={n}, maxSum={max_sum})"
        for banned, n, max_sum in sorted(cases)
    ]
