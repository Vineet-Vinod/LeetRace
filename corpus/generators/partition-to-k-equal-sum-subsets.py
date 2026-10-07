import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((4, 3, 2, 3, 5, 2, 1), 4),
        ((1, 2, 3, 4), 3),
        ((1,), 1),
        ((2, 2, 2, 2), 2),
        ((1, 1, 1, 1), 4),
        ((10_000,) * 4, 4),
        ((1, 1, 1, 1, 10_000), 3),
        (tuple(range(1, 17)), 8),
    }
    while len(cases) < 600:
        n = rng.randint(1, 16)
        nums = tuple(rng.randint(1, 20) for _ in range(n))
        if max(nums.count(value) for value in set(nums)) > 4:
            continue
        cases.add((nums, rng.randint(1, n)))
        # Construct feasible cases with varied bucket sums as well.
        if n >= 2:
            k = rng.randint(2, min(n, 8))
            target = rng.randint(20, 80)
            generated = tuple(
                value for index in range(k) for value in (index + 1, target - index - 1)
            )
            if max(generated.count(value) for value in set(generated)) <= 4:
                cases.add((generated, k))
    assert all(
        1 <= k <= len(nums) <= 16
        and all(1 <= value <= 10_000 for value in nums)
        and max(nums.count(value) for value in set(nums)) <= 4
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
