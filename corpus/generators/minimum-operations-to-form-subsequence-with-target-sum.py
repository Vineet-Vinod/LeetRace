import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["nums"]
        target = args["target"]
        assert 1 <= len(a) <= 1000 and all(
            1 <= x <= 2**30 and x & (x - 1) == 0 for x in a
        )
        assert 1 <= target < 2**31
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(nums=[1, 2, 8], target=7)
    add(nums=[1, 32, 1, 2], target=12)
    add(nums=[1, 32, 1], target=35)
    add(nums=[2**30] * 1000, target=2**31 - 1)
    add(nums=[1] * 1000, target=1000)
    add(nums=[1, 2, 8], target=7)
    add(nums=[1, 32, 1, 2], target=12)
    add(nums=[1, 32, 1], target=35)
    while len(calls) < 600:
        a = [2 ** rng.randint(0, 12) for _ in range(rng.randint(1, 50))]
        mode = len(calls) % 3
        if mode == 0:
            target = sum(a[::2])
        elif mode == 1:
            a = [2 ** rng.randint(9, 30) for _ in range(rng.randint(1, 50))]
            target = 2 * rng.randint(0, 255) + 1
        else:
            target = sum(a) + rng.randint(1, 100)
        add(nums=a, target=target)
    return list(calls)[:600]
