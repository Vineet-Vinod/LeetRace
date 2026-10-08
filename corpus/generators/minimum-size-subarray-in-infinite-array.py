def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(nums: list[int], target: int) -> None:
        assert 1 <= len(nums) <= 100_000
        assert all(1 <= value <= 100_000 for value in nums)
        assert 1 <= target <= 1_000_000_000
        cases.add(f"candidate(nums={nums!r}, target={target})")

    add([1, 2, 3], 5)
    add([2, 4, 6, 8], 3)
    add([1] * 100_000, 100_000)
    add([1], 1_000_000_000)
    add([100_000], 100_000)

    # For all-ones arrays the shortest infinite-array subarray has length target.
    for target in range(1, 301):
        add([1], target)

    # Even-valued inputs cannot sum to an odd target, guaranteeing no solution.
    for target in range(1, 601, 2):
        add([2 + (target % 100) * 2] * (1 + target % 30), target)

    while len(cases) < 600:
        size = rng.randint(1, 100)
        nums = [rng.randint(1, 100_000) for _ in range(size)]
        total = sum(nums)
        if rng.random() < 0.55:
            target = rng.randint(1, min(1_000_000_000, total * 3))
        else:
            target = rng.randint(1, 1_000_000_000)
        add(nums, target)

    result = list(cases)
    rng.shuffle(result)
    return result
