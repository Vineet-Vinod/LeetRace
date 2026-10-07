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
        array(d["stones"], 1, 100, 30)
        assert 2 <= d["k"] <= 30

    add(stones=[100] * 30, k=2)
    add(stones=[100] * 30, k=30)
    add(stones=[1] * 30, k=29)
    add(stones=[3, 2, 4, 1], k=2)
    add(stones=[3, 2, 4, 1], k=3)
    add(stones=[3, 5, 1, 2, 6], k=3)
    while len(calls) < 600:
        stones = [rng.randint(1, 100) for _ in range(rng.randint(1, 20))]
        k = 2 if rng.randrange(2) else rng.randint(2, 30)
        add(stones=stones, k=k)
    assert len(calls) == 600
    return calls
