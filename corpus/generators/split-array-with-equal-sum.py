import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(nums: list[int]) -> None:
        assert 1 <= len(nums) <= 2000 and all(-(10**6) <= v <= 10**6 for v in nums)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("nums", nums)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1, 2, 1, 2, 1, 2, 1])
    add(nums=[0] * 2000)
    add(nums=[10**6] * 2000)
    add(nums=[-(10**6)] * 2000)
    add(nums=[1, 2, 1, 2, 1, 2, 1])
    add(nums=[1, 2, 1, 2, 1, 2, 1, 2])
    while len(calls) < 600:
        if len(calls) % 2 == 0:
            target = rng.randint(-20, 20)
            nums = []
            for j in range(4):
                part = [rng.randint(-10, 10) for _ in range(rng.randint(0, 6))]
                part.append(target - sum(part))
                nums.extend(part)
                if j < 3:
                    nums.append(rng.randint(-20, 20))
        else:
            nums = [rng.randint(-100, 100) for _ in range(rng.randint(1, 40))]
        add(nums=nums)
    return calls
