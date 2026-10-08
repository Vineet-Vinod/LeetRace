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
        n = d["n"]
        assert n.isdigit() and n[0] != "0" and 1 <= int(n) <= 10**18 - 1

    for digits in range(1, 19):
        for v in (10 ** (digits - 1), 10**digits - 1):
            add(n=str(v))
    add(n="123")
    add(n="1")
    while len(calls) < 600:
        v = rng.randint(1, 10 ** rng.randint(1, 18) - 1)
        add(n=str(v))
    assert len(calls) == 600
    return calls
