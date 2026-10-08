import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b = kwargs["nums1"], kwargs["nums2"]
        assert 3 <= len(a) == len(b) <= 100000
        assert sorted(a) == sorted(b) == list(range(len(a)))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums1=[2, 0, 1, 3], nums2=[0, 1, 2, 3])
    add(nums1=[4, 0, 1, 3, 2], nums2=[4, 1, 0, 2, 3])
    add(nums1=list(range(100000)), nums2=list(range(100000)))
    add(nums1=list(range(100000)), nums2=list(reversed(range(100000))))
    while len(calls) < 600:
        n = rng.randint(3, 45)
        a = list(range(n))
        rng.shuffle(a)
        b = a.copy()
        if len(calls) % 3 == 1:
            b.reverse()
        elif len(calls) % 3 == 2:
            rng.shuffle(b)
        add(nums1=a, nums2=b)
    return calls
