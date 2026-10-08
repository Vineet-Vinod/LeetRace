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
        array(d["nums"], 1, 20000, 20000)
        assert 1 <= d["low"] <= d["high"] <= 20000

    add(nums=[1, 4, 2, 7], low=2, high=6)
    add(nums=[9, 8, 4, 2, 1], low=5, high=14)
    add(nums=[20000] * 20000, low=1, high=20000)
    add(nums=[1, 20000] * 10000, low=1, high=20000)
    while len(calls) < 600:
        nums = [
            rng.randint(1, 20000 if rng.randrange(3) == 0 else 64)
            for _ in range(rng.randint(1, 70))
        ]
        lo = rng.randint(1, 20000) if rng.randrange(4) == 0 else rng.randint(1, 32)
        hi = rng.randint(lo, 20000 if lo > 64 else 64)
        add(nums=nums, low=lo, high=hi)
    assert len(calls) == 600
    return calls
