import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, b, k = data["nums1"], data["nums2"], data["k"]
        assert (
            1 <= len(a) <= 50000 and 1 <= len(b) <= 50000 and 1 <= k <= len(a) * len(b)
        )
        assert (
            a == sorted(a)
            and b == sorted(b)
            and all(-100000 <= x <= 100000 for x in a + b)
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"nums1": [2, 5], "nums2": [3, 4], "k": 2},
        {"nums1": [-4, -2, 0, 3], "nums2": [2, 4], "k": 6},
        {"nums1": [-2, -1, 0, 1, 2], "nums2": [-3, -1, 2, 4, 5], "k": 3},
    ]:
        add(**example)
    add(
        nums1=[-100000] * 25000 + [100000] * 25000,
        nums2=[-100000] * 25000 + [100000] * 25000,
        k=1250000001,
    )
    add(nums1=[-100000], nums2=[100000], k=1)
    add(nums1=[0] * 50000, nums2=[-100000] * 50000, k=2500000000)
    while len(calls) < 600:
        mode = len(calls) % 4
        low, high = (
            (-100000, 100000)
            if mode == 0
            else (-10, 10)
            if mode == 1
            else (-100, -1)
            if mode == 2
            else (1, 100)
        )
        a = sorted(rng.randint(low, high) for _ in range(rng.randint(1, 20)))
        b = sorted(rng.randint(-100, 100) for _ in range(rng.randint(1, 20)))
        k = rng.choice([1, len(a) * len(b), rng.randint(1, len(a) * len(b))])
        add(nums1=a, nums2=b, k=k)
    assert len(calls) == 600
    return calls
