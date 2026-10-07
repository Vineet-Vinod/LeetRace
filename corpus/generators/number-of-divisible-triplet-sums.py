def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(nums: list[int], divisor: int) -> None:
        assert 1 <= len(nums) <= 1000
        assert all(1 <= value <= 1_000_000_000 for value in nums)
        assert 1 <= divisor <= 1_000_000_000
        cases.add(f"candidate(nums={nums!r}, d={divisor})")

    add([3, 3, 4, 7, 8], 5)
    add([1] * 1000, 3)
    add([1] * 1000, 1_000_000_000)
    add([1_000_000_000] * 3, 1_000_000_000)

    # All values congruent to 1 modulo 3 create many divisible triplets.
    for index in range(200):
        size = 3 + index % 998
        value = 1 + 3 * (index % 1000)
        add([value] * size, 3)

    # Sums remain below the divisor, guaranteeing no divisible triplets.
    for index in range(200):
        size = 3 + index % 998
        divisor = 3 * size + 1
        add([1] * size, divisor)

    # Small divisors and residue patterns intentionally create varied counts.
    for index in range(200):
        size = 1 + index % 1000
        divisor = rng.randint(2, 20)
        nums = [rng.randint(1, 1000) for _ in range(size)]
        add(nums, divisor)

    while len(cases) < 600:
        size = rng.randint(1, 1000)
        divisor = rng.randint(1, 1_000_000_000)
        nums = [rng.randint(1, 1_000_000_000) for _ in range(size)]
        add(nums, divisor)

    result = list(cases)
    rng.shuffle(result)
    return result
