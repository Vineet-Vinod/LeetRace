import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(nums1, nums2):
        n = len(nums1)
        assert 2 <= n <= 100000 and len(nums2) == n
        assert all(0 <= x <= n for x in nums1 + nums2)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("nums1", nums1),
                    ("nums2", nums2),
                )
            )
            + ")"
        )
        calls[call] = None

    add(nums1=[1, 2, 3, 2, 4], nums2=[2, 3, 1, 2, 3])
    add(nums1=[1, 2, 4, 3, 2, 5], nums2=[1, 4, 2, 3, 5, 1])
    add(nums1=list(range(99999)) + [100000], nums2=[0] * 99999 + [100000])
    add(nums1=[0, 2], nums2=[2, 0])
    add(nums1=[0, 2, 0, 2], nums2=[0, 0, 2, 2])
    while len(calls) < 600:
        n = rng.randint(2, 40)
        mode = rng.randrange(4)
        x = [rng.randint(0, n) for _ in range(n)]
        y = [rng.randint(0, n) for _ in range(n)]
        if mode == 0:
            x[-1], y[-1] = x[0], y[0]
        elif mode == 1:
            y = [rng.randint(0, n)] * n
        elif mode == 2:
            x = list(range(n))
            rng.shuffle(x)
        add(nums1=x, nums2=y)
    return list(calls)
