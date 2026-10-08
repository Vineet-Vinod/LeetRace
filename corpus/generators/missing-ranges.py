import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((), 0, 0),
        ((0, 1, 3, 50, 75), 0, 99),
        ((-1,), -1, -1),
    }
    cases.add(((-1_000_000_000, 0, 1_000_000_000), -1_000_000_000, 1_000_000_000))
    cases.add((tuple(range(-50, 50)), -1_000_000_000, 1_000_000_000))
    while len(cases) < 600:
        lower = rng.randint(-1_000_000_000, 1_000_000_000)
        upper = min(1_000_000_000, lower + rng.randint(0, 1000))
        nums = tuple(
            sorted(
                rng.sample(
                    range(lower, upper + 1), rng.randint(0, min(100, upper - lower + 1))
                )
            )
        )
        cases.add((nums, lower, upper))
    return [
        f"candidate(nums={list(nums)!r}, lower={lower}, upper={upper})"
        for nums, lower, upper in cases
    ]
