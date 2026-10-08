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
        assert len(a) == len(b)
        array(a, 1, len(a), 100000)
        array(b, 1, len(b), 100000)

    add(nums1=list(range(1, 100001)), nums2=list(range(1, 100001)))
    add(nums1=[1] * 100000, nums2=[1] * 100000)
    add(nums1=[1, 2, 3, 4, 5], nums2=[1, 2, 3, 4, 5])
    add(nums1=[2, 2, 2, 1, 3], nums2=[1, 2, 2, 3, 3])
    while len(calls) < 600:
        n = rng.randint(1, 80)
        a = [rng.randint(1, rng.choice([min(2, n), n])) for _ in range(n)]
        b = a[:] if rng.randrange(3) == 0 else [rng.randint(1, n) for _ in range(n)]
        add(nums1=a, nums2=b)
    assert len(calls) == 600
    return calls
