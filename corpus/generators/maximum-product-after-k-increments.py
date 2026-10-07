import random


def generate(seed: int = 0) -> list[str]:
    """Generate arrays length and k in 1..100000 with values 0..1000000."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[0, 4], k=5)",
        "candidate(nums=[6, 3, 3, 2], k=2)",
        "candidate(nums=[0] * 100000, k=100000)",
        "candidate(nums=[1000000] + [0] * 99999, k=100000)",
    }
    while len(calls) < 600:
        nums = [
            rng.choice([0, 1, 10**6, rng.randint(0, 10**6)])
            for _ in range(rng.randint(1, 200))
        ]
        k = rng.choice([1, 100_000, rng.randint(1, 100_000)])
        assert 1 <= len(nums) <= 100_000 and all(0 <= value <= 10**6 for value in nums)
        assert 1 <= k <= 100_000
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)
