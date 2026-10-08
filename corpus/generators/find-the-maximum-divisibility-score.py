import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((2, 9, 15, 50), (5, 3, 7, 2)),
        ((1,), (1,)),
        (tuple(range(1, 1001)), tuple(range(1, 1001))),
    }
    cases.add(((1, 10**9) * 500, (1, 10**9) * 500))
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 1_000_000_000) for _ in range(rng.randint(1, 80)))
        divisors = tuple(
            rng.randint(1, 1_000_000_000) for _ in range(rng.randint(1, 80))
        )
        cases.add((nums, divisors))
    calls = [
        f"candidate(nums={list(nums)!r}, divisors={list(divisors)!r})"
        for nums, divisors in cases
    ]
    calls.extend(
        [
            "candidate(nums=[4, 7, 9, 3, 9], divisors=[5, 2, 3])",
            "candidate(nums=[20, 14, 21, 10], divisors=[10, 16, 20])",
        ]
    )
    return list(dict.fromkeys(calls))
