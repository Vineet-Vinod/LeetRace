import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[tuple[int, ...], int]] = set()

    def add(nums: list[int], k: int) -> None:
        key = (tuple(nums), k)
        if key not in seen:
            assert 1 <= len(nums) <= 100_000
            assert 1 <= k <= 100_000
            assert all(-10_000 <= value <= 10_000 for value in nums)
            seen.add(key)
            cases.append(f"candidate(nums={nums!r}, k={k})")

    add([1, -1, -2, 4, -7, 3], 2)
    add([10, -5, -2, 4, 0, 3], 3)
    add([1, -5, -20, 4, -1, 3, -6, -3], 2)
    add([42], 100_000)
    add([1] * 100_000, 1)
    add([10_000] * 100_000, 100_000)

    while len(cases) < 600:
        nums = [rng.randint(-10_000, 10_000) for _ in range(rng.randint(1, 100))]
        k = rng.randint(1, 100_000)
        add(nums, k)
    return cases
