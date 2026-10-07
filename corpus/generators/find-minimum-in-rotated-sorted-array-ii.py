import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        nums = kwargs["nums"]
        assert 1 <= len(nums) <= 5000 and all(-5000 <= x <= 5000 for x in nums)
        assert sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums))) <= 1
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[5000] * 4999 + [-5000])
    add(nums=[-5000] * 5000)
    add(nums=[1, 3, 5])
    add(nums=[2, 2, 2, 0, 1])
    while len(calls) < 600:
        nums = sorted(rng.choices(range(-5000, 5001), k=rng.randint(1, 80)))
        if len(calls) % 3 == 0:
            nums = sorted(rng.choices(range(-3, 4), k=rng.randint(1, 80)))
        cut = rng.randrange(len(nums))
        nums = nums[cut:] + nums[:cut]
        add(nums=nums)
    return calls
