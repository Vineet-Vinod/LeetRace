import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        for a in (d["nums1"], d["nums2"]):
            assert (
                1 <= len(a) <= 100000
                and all(1 <= v <= 10**7 for v in a)
                and all(x < y for x, y in zip(a, a[1:]))
            )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums1=[2, 4, 5, 8, 10], nums2=[4, 6, 8, 9])
    add(nums1=[1, 3, 5, 7, 9], nums2=[3, 5, 100])
    add(nums1=[1, 2, 3, 4, 5], nums2=[6, 7, 8, 9, 10])
    add(nums1=list(range(1, 100001)), nums2=list(range(9900001, 10000001)))
    add(nums1=list(range(9900001, 10000001)), nums2=list(range(9900001, 10000001)))
    t = 0
    while len(calls) < 600:
        if t % 3 == 0:
            pool = rng.sample(range(1, 150), rng.randint(2, 50))
            a = sorted(pool[::2])
            b = sorted(pool[1::2])
        else:
            a = sorted(rng.sample(range(1, 150), rng.randint(1, 40)))
            b = sorted(rng.sample(range(1, 150), rng.randint(1, 40)))
        add(nums1=a, nums2=b)
        t += 1
    return calls
