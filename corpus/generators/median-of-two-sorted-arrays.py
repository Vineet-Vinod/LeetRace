import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kwargs.items()) + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(text):
        return all("a" <= ch <= "z" for ch in text)

    def array(values, minimum, maximum, length):
        assert 1 <= len(values) <= length
        assert all(minimum <= v <= maximum for v in values)

    def validate(d):
        a, b = d["nums1"], d["nums2"]
        assert (
            0 <= len(a) <= 1000 and 0 <= len(b) <= 1000 and 1 <= len(a) + len(b) <= 2000
        )
        assert a == sorted(a) and b == sorted(b)
        assert all(-1000000 <= v <= 1000000 for v in a + b)

    add(nums1=[-1000000] * 1000, nums2=[1000000] * 1000)
    add(nums1=[], nums2=[-1000000])
    add(nums1=[1, 3], nums2=[2])
    add(nums1=[1, 2], nums2=[3, 4])
    while len(calls) < 600:
        a = sorted(rng.randint(-1000000, 1000000) for _ in range(rng.randint(0, 60)))
        b = sorted(rng.randint(-1000000, 1000000) for _ in range(rng.randint(1, 60)))
        add(nums1=a, nums2=b)
    assert len(calls) == 600
    return calls
