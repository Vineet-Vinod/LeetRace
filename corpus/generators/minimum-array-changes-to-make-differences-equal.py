def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(nums: list[int], k: int) -> None:
        assert 2 <= len(nums) <= 100_000 and len(nums) % 2 == 0
        assert 0 <= k <= 100_000 and all(0 <= value <= k for value in nums)
        cases.add(f"candidate(nums={nums!r}, k={k})")

    # Include the zero-boundary and maximum length/value constraints.
    add([0, 0], 0)
    add([0, 100_000], 100_000)
    add([0] * 100_000, 100_000)
    add([0] * 100_000, 0)
    add([100_000 if index % 2 else 0 for index in range(100_000)], 100_000)

    # Identical and deliberately mismatched pair differences cover zero and
    # positive minimum-change outcomes with low and high target differences.
    for k in range(1, 41):
        for target in (0, k // 2, k):
            nums = []
            for pair in range(1 + (k + target) % 8):
                left = min(k - target, (pair * 3) % (k + 1))
                nums.extend((left, left + target))
            add(nums, k)
        nums = []
        for pair in range(1 + k % 8):
            left = pair % (k + 1)
            right = (left + pair + 1) % (k + 1)
            nums.extend((left, right))
        add(nums, k)

    while len(cases) < 600:
        k = rng.randint(0, 100_000)
        pair_count = rng.randint(1, 100)
        pattern = rng.randrange(4)
        nums: list[int] = []
        if pattern == 0:
            # All pairs realize the same target difference, so zero changes suffice.
            target = rng.randint(0, k)
            for _ in range(pair_count):
                left = rng.randint(0, k - target)
                nums.extend((left, left + target))
        elif pattern == 1:
            # Exact matching values create many already-equal pairs.
            for _ in range(pair_count):
                value = rng.randint(0, k)
                nums.extend((value, value))
        else:
            nums = [rng.randint(0, k) for _ in range(2 * pair_count)]
        add(nums, k)

    result = list(cases)
    rng.shuffle(result)
    return result
