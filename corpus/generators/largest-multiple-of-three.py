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
        array(d["digits"], 0, 9, 10000)

    add(digits=[9] * 10000)
    add(digits=[0] * 10000)
    add(digits=[8, 1, 9])
    add(digits=[8, 6, 7, 1, 0])
    add(digits=[1])
    # These 24 calls enumerate every impossible digit array: length >= 3
    # always has either a mixed remainder pair or three equal remainders.
    for remainder in (1, 2):
        digits = [d for d in range(1, 10) if d % 3 == remainder]
        for d in digits:
            add(digits=[d])
        for a in digits:
            for b in digits:
                add(digits=[a, b])
    while len(calls) < 600:
        add(digits=[rng.randint(0, 9) for _ in range(rng.randint(1, 70))])
    assert len(calls) == 600
    return calls
