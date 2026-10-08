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
        array(d["arr"], 1, 10**6, 10**5)
        assert 0 <= d["target"] <= 10**7

    add(arr=[9, 12, 3, 7, 15], target=5)
    add(arr=[10**6] * 100000, target=10**7)
    add(arr=[1, 2] * 50000, target=0)
    while len(calls) < 600:
        arr = [rng.randint(1, 1000000) for _ in range(rng.randint(1, 70))]
        target = rng.choice([0, 10000000, rng.choice(arr), rng.randint(1, 1000000)])
        add(arr=arr, target=target)
    assert len(calls) == 600
    return calls
