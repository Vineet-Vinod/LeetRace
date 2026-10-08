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
        assert 1 <= d["n"] <= 20000

    add(n=20000)
    add(n=19999)
    while len(calls) < 600:
        add(n=rng.randint(1, 750))
    assert len(calls) == 600
    return calls
