import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[1000000000] * 12)
    add(nums=[0] * 12)
    add(nums=[2] * 12)
    while len(calls) < 600:
        n = rng.randint(1, 10)
        if len(calls) % 2 == 0:
            # Construct an explicit squareful walk; random ordering preserves its existence.
            nums = [rng.randint(0, 100)]
            for _ in range(n - 1):
                root = rng.randint(int(nums[-1] ** 0.5) + 1, int(nums[-1] ** 0.5) + 10)
                nums.append(root * root - nums[-1])
            rng.shuffle(nums)
        else:
            nums = [rng.randint(0, 50) for _ in range(n)]
        assert 1 <= len(nums) <= 12 and all(0 <= x <= 10**9 for x in nums)
        add(nums=nums)
    assert len(calls) == 600
    return list(calls)
