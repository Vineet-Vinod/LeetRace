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
        array(d["nums"], 0, 1000, 1000)

    add(nums=[0, 1000] * 500)
    add(nums=list(range(1000)))
    add(nums=[3, 2, 4, 5, 0])
    add(nums=[0])
    while len(calls) < 600:
        nums = [rng.randint(0, 1000) for _ in range(rng.randint(1, 80))]
        if rng.randrange(4) == 0:
            nums.sort(reverse=bool(rng.randrange(2)))
        add(nums=nums)
    assert len(calls) == 600
    return calls
