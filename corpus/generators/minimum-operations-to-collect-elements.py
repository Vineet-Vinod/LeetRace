import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 50)
        k = rng.randint(1, size)
        nums = list(range(1, k + 1)) + [rng.randint(1, size) for _ in range(size - k)]
        rng.shuffle(nums)
        assert all(1 <= value <= size for value in nums) and set(
            range(1, k + 1)
        ) <= set(nums)
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)
