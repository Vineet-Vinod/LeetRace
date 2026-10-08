import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((0, 1, 2, 3), (0, 1, 3)),
        ((0, 1, 2, 3, 4), (0, 3, 1, 4)),
        ((0,), (0,)),
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        values = tuple(rng.sample(range(size), size))
        nums = tuple(rng.sample(values, rng.randint(1, size)))
        cases.add((values, nums))
    assert all(
        1 <= len(values) <= 10_000
        and 1 <= len(nums) <= len(values)
        and set(values) == set(range(len(values)))
        and len(set(nums)) == len(nums)
        and set(nums) <= set(values)
        for values, nums in cases
    )
    return [
        f"candidate(head=list_node({list(values)!r}), nums={list(nums)!r})"
        for values, nums in sorted(cases)
    ]
