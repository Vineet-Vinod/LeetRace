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
        array(d["nums"], 1, 20000, 100000)
        assert 0 <= d["k"] < len(d["nums"])

    add(nums=[20000] * 100000, k=99999)
    add(nums=[1, 20000] * 50000, k=0)
    add(nums=[1, 4, 3, 7, 4, 5], k=3)
    while len(calls) < 600:
        nums = [rng.randint(1, 20000) for _ in range(rng.randint(1, 80))]
        add(nums=nums, k=rng.choice([0, len(nums) - 1, rng.randrange(len(nums))]))
    assert len(calls) == 600
    return calls
