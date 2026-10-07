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
        array(d["arr"], 0, 1, 30000)
        assert len(d["arr"]) >= 3

    add(arr=[0] * 30000)
    add(arr=[1, 0] * 15000)
    add(arr=[1, 0, 1, 0, 1])
    add(arr=[1, 1, 0, 1, 1])
    add(arr=[1, 1, 0, 0, 1])
    while len(calls) < 600:
        if rng.randrange(2):
            pattern = [1] + [rng.randrange(2) for _ in range(rng.randint(0, 25))]
            arr = (
                [0] * rng.randint(0, 10)
                + pattern
                + [0] * rng.randint(0, 10)
                + pattern
                + [0] * rng.randint(0, 10)
                + pattern
            )
        else:
            arr = [rng.randrange(2) for _ in range(rng.randint(3, 100))]
        add(arr=arr)
    assert len(calls) == 600
    return calls
