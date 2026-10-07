import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        nums = kwargs["nums"]
        assert 1 <= len(nums) <= 100000 and all(
            -(2**31) <= v <= 2**31 - 1 for v in nums
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=list(range(1, 100001)))
    add(nums=[-(2**31), 2**31 - 1] * 50000)
    add(nums=[1, 2, 0])
    add(nums=[3, 4, -1, 1])
    add(nums=[7, 8, 9, 11, 12])
    while len(calls) < 600:
        n = rng.randint(1, 70)
        if len(calls) % 2:
            nums = list(range(1, n + 1))
            nums[rng.randrange(n)] = rng.choice([0, -1, 2**31 - 1])
            rng.shuffle(nums)
        else:
            nums = [rng.randint(-n, n + 3) for _ in range(n)]
        add(nums=nums)
    return calls
