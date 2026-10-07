import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(nums, k):
        assert 1 <= k <= len(nums) <= 100000 and all(
            -2147483648 <= v <= 2147483647 for v in nums
        )
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

    add(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
    add(nums=[1, 2, 3, 4, 2, 3, 1, 4, 2], k=3)
    add(nums=list(range(100000)), k=50000)
    add(nums=[2147483647, -2147483648] * 50000, k=2)
    add(nums=[2147483647] * 100000, k=100000)
    add(nums=[-2147483648], k=1)
    while len(calls) < 600:
        n = rng.randint(1, 70)
        mode = rng.randrange(5)
        nums = [rng.randint(-20, 20) for _ in range(n)]
        if mode == 0:
            nums = [rng.choice((-2147483648, 2147483647)) for _ in range(n)]
        elif mode == 1:
            nums.sort()
        elif mode == 2:
            nums.sort(reverse=True)
        elif mode == 3:
            nums = [rng.randint(-2147483648, 2147483647)] * n
        k = rng.choice((1, n)) if mode == 4 else rng.randint(1, n)
        add(nums=nums, k=k)
    return list(calls)
