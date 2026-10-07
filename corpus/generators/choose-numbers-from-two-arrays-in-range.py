import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b = kwargs["nums1"], kwargs["nums2"]
        assert 1 <= len(a) == len(b) <= 100
        assert all(0 <= x <= 100 for x in a + b)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums1=[1, 2, 5], nums2=[2, 6, 3])
    add(nums1=[0, 1], nums2=[1, 0])
    add(nums1=[0] * 100, nums2=[0] * 100)
    add(nums1=[100] * 100, nums2=[100] * 100)
    add(nums1=[0], nums2=[0])
    add(nums1=[100], nums2=[100])
    while len(calls) < 600:
        n = rng.randint(1, 12)
        a = [rng.randint(0, 12) for _ in range(n)]
        b = a.copy() if len(calls) % 3 == 0 else [rng.randint(0, 12) for _ in range(n)]
        add(nums1=a, nums2=b)
    return calls
