import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((1, -3, 4), 1, 6),
        ((3, -4, 5, 1, -2), -4, 5),
        ((4, -7, 2), 3, 6),
        ((0,) * 100_000, -100_000, 100_000),
        ((100_000, -100_000) * 50_000, -100_000, 100_000),
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        if rng.random() < 0.7:
            differences = tuple(rng.randint(-20, 20) for _ in range(size))
            prefix = [0]
            for difference in differences:
                prefix.append(prefix[-1] + difference)
            slack = rng.randint(0, 100)
            lower = min(prefix) - slack
            upper = max(prefix) + slack
            shift = rng.randint(-100_000 - lower, 100_000 - upper)
            lower += shift
            upper += shift
        else:
            differences = tuple(rng.randint(-(10**5), 10**5) for _ in range(size))
            lower, upper = sorted(
                (rng.randint(-(10**5), 10**5), rng.randint(-(10**5), 10**5))
            )
        cases.add((differences, lower, upper))
    assert all(
        1 <= len(differences) <= 100_000
        and all(-(10**5) <= value <= 10**5 for value in differences)
        and -(10**5) <= lower <= upper <= 10**5
        for differences, lower, upper in cases
    )
    return [
        f"candidate(differences={list(d)!r}, lower={lo}, upper={hi})"
        for d, lo, hi in sorted(cases)
    ]
