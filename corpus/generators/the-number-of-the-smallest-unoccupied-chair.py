import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], int]] = {
        (((1, 4), (2, 3), (4, 6)), 1),
        (((3, 10), (1, 5), (2, 6)), 0),
        (((1, 2), (2, 3)), 1),
        (tuple((i + 1, i + 10_001) for i in range(10_000)), 9_999),
        (((99_999, 100_000), (1, 99_998)), 0),
    }
    while len(cases) < 600:
        n = rng.randint(2, 40)
        arrivals = rng.sample(range(1, 99_001), n)
        times = tuple(
            (start, start + rng.randint(1, 100_000 - start)) for start in arrivals
        )
        cases.add((times, rng.randrange(n)))
    assert all(
        2 <= len(times) <= 10_000
        and 0 <= target < len(times)
        and len({arrival for arrival, _ in times}) == len(times)
        and all(1 <= arrival < leaving <= 100_000 for arrival, leaving in times)
        for times, target in cases
    )
    return [
        f"candidate(times={list(times)!r}, targetFriend={target})"
        for times, target in sorted(cases)
    ]
