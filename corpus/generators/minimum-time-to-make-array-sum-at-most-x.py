import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a, b = args["nums1"], args["nums2"]
        assert 1 <= len(a) == len(b) <= 1000
        assert all(1 <= v <= 1000 for v in a) and all(0 <= v <= 1000 for v in b)
        assert 0 <= args["x"] <= 1000000
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(nums1=[1, 2, 3], nums2=[1, 2, 3], x=4)
    add(nums1=[1, 2, 3], nums2=[3, 3, 3], x=4)
    add(nums1=[1000] * 1000, nums2=[1000] * 1000, x=1000000)
    add(nums1=[1000] * 1000, nums2=[0] * 1000, x=0)
    add(nums1=[1, 2, 3], nums2=[1, 2, 3], x=4)
    add(nums1=[1, 2, 3], nums2=[3, 3, 3], x=4)
    while len(calls) < 600:
        n = rng.randint(1, 30)
        a = [rng.randint(1, 1000) for _ in range(n)]
        mode = len(calls) % 4
        b = [rng.randint(0, 1000) for _ in range(n)]
        if mode == 0:
            b = [0] * n
            x = rng.randint(0, sum(a))
        elif mode == 1:
            x = sum(a)
        elif mode == 2:
            b = [1000] * n
            x = 0
        else:
            x = rng.randint(0, sum(a))
        add(nums1=a, nums2=b, x=x)
    return list(calls)[:600]
