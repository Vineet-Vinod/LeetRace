import random


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of length 1..100000, values 1..10^9, and k in 1..10^8."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 4, 25, 10, 25], k=2)",
        "candidate(nums=[5, 6], k=6)",
        "candidate(nums=list(range(1, 100001)), k=100000000)",
        "candidate(nums=[1000000000] * 100000, k=100000000)",
    }
    while len(calls) < 600:
        length = rng.randint(1, 200)
        nums = [rng.choice([1, 2, 10**9, rng.randint(1, 10**9)]) for _ in range(length)]
        k = rng.choice([1, 100_000_000, rng.randint(1, 100_000_000)])
        assert 1 <= len(nums) <= 100_000 and all(1 <= value <= 10**9 for value in nums)
        assert 1 <= k <= 10**8
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)
