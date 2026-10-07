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
        array(d["prices"], 1, 100000, 100000)

    add(prices=[100000] * 100000)
    add(prices=[1, 100000] * 50000)
    add(prices=[3, 1, 2])
    add(prices=[1, 10, 1, 1])
    while len(calls) < 600:
        add(prices=[rng.randint(1, 100000) for _ in range(rng.randint(1, 100))])
    assert len(calls) == 600
    return calls
