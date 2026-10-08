import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(nums, k):
        assert 1 <= k <= len(nums) <= 2000
        assert all(0 <= v < 1024 for v in nums)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("nums", nums),
                    ("k", k),
                )
            )
            + ")"
        )
        calls[call] = None

    add(nums=[1, 2, 0, 3, 0], k=1)
    add(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3)
    add(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3)
    add(nums=[1023 if i % 3 else 0 for i in range(2000)], k=1000)
    add(nums=[1023] * 2000, k=1)
    add(nums=[0] * 2000, k=2000)
    while len(calls) < 600:
        n = rng.randint(1, 30)
        k = rng.randint(1, n)
        mode = rng.randrange(4)
        if mode == 0:
            block = [rng.randint(0, 7) for _ in range(k - 1)]
            last = 0
            for v in block:
                last ^= v
            block.append(last)
            nums = [block[i % k] for i in range(n)]
        elif mode == 1:
            nums = [rng.randint(0, 7) for _ in range(n)]
        elif mode == 2:
            nums = [rng.randint(0, 7)] * n
        else:
            nums = [rng.randint(0, 31) for _ in range(n)]
        add(nums=nums, k=k)
    return list(calls)
