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
        array(d["nums"], -10000, 10000, 10000)
        assert 1 <= d["k"] <= len(d["nums"])

    add(nums=[1, 12, -5, -6, 50, 3], k=4)
    add(nums=[-10000, 10000] * 5000, k=1)
    add(nums=[10000] * 10000, k=10000)
    add(nums=list(range(-5000, 5000)), k=5000)
    while len(calls) < 600:
        nums = [rng.randint(-10000, 10000) for _ in range(rng.randint(1, 50))]
        add(nums=nums, k=rng.randint(1, len(nums)))
    assert len(calls) == 600
    return calls
