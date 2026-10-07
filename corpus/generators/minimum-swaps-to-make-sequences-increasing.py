import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b = kwargs["nums1"], kwargs["nums2"]
        assert 2 <= len(a) == len(b) <= 100000
        assert all(0 <= x <= 200000 for x in a + b)
        # Sorting each column into its lower/upper values preserves a known increasing witness.
        low = [min(x, y) for x, y in zip(a, b)]
        high = [max(x, y) for x, y in zip(a, b)]
        assert all(x < y for x, y in zip(low, low[1:])) and all(
            x < y for x, y in zip(high, high[1:])
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums1=[1, 3, 5, 4], nums2=[1, 2, 3, 7])
    add(nums1=[0, 3, 5, 8, 9], nums2=[2, 1, 4, 6, 9])
    add(nums1=list(range(2, 200001, 2)), nums2=list(range(1, 200000, 2)))
    while len(calls) < 600:
        n = rng.randint(2, 90)
        a = []
        b = []
        x, y = rng.randint(0, 20), rng.randint(0, 20)
        for _ in range(n):
            x += rng.randint(1, 8)
            y += rng.randint(1, 8)
            if rng.randrange(2):
                a.append(x)
                b.append(y)
            else:
                a.append(y)
                b.append(x)
        add(nums1=a, nums2=b)
    return calls
