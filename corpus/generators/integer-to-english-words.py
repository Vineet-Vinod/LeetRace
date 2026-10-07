import random


def literal(value):
    if isinstance(value, list):
        if len(value) > 30 and all(x == value[0] for x in value):
            return f"[{literal(value[0])}] * {len(value)}"
        if len(value) > 30 and all(isinstance(x, int) for x in value):
            step = value[1] - value[0]
            if step and all(x == value[0] + i * step for i, x in enumerate(value)):
                return f"list(range({value[0]}, {value[-1] + step}, {step}))"
        return "[" + ", ".join(literal(x) for x in value) + "]"
    return repr(value)


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(*args):
        validate(*args)
        call = "candidate(" + ", ".join(literal(x) for x in args) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(123)
    add(12345)
    add(1234567)

    for n in [
        0,
        1,
        19,
        20,
        21,
        99,
        100,
        101,
        110,
        1000,
        1001,
        1010,
        1100,
        1000000,
        1000001,
        1001000,
        1000000000,
        1000000001,
        2**31 - 1,
    ]:
        add(n)

    while len(calls) < 600:
        mode = len(calls) % 4
        if mode == 0:
            n = rng.randint(1, 999) * rng.choice([1, 1000, 10**6])
        elif mode == 1:
            n = rng.randint(0, 2) * 10**9 + rng.randint(0, 999)
        else:
            n = rng.randint(0, 2**31 - 1)
        add(n)
    return calls


def validate(n):
    assert 0 <= n <= 2**31 - 1
