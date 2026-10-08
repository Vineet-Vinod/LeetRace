import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=list(range(1, 501)) + list(range(500, 0, -1)))
    add(nums=[1, 1000000000, 1] + [1000000000] * 997)
    while len(calls) < 600:
        nums = [rng.randint(1, 50) for _ in range(rng.randint(3, 45))]
        # A strict 1, 10^9, 1 subsequence guarantees the promised mountain exists.
        positions = sorted(rng.sample(range(len(nums)), 3))
        for i, x in zip(positions, [1, 1000000000, 1]):
            nums[i] = x
        assert 3 <= len(nums) <= 1000 and all(1 <= x <= 10**9 for x in nums)
        assert nums[positions[0]] < nums[positions[1]] > nums[positions[2]]
        add(nums=nums)
    assert len(calls) == 600
    return list(calls)
