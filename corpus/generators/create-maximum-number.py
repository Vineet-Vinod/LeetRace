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

    add([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
    add([6, 7], [6, 0, 4], 5)
    add([3, 9], [8, 9], 3)

    add([9] * 500, [9] * 500, 1000)
    add([1] + [0] * 499, [2] + [0] * 499, 1)
    add([1], [9], 1)

    while len(calls) < 600:
        a = [rng.randint(0, 9) for _ in range(rng.randint(1, 16))]
        b = [rng.randint(0, 9) for _ in range(rng.randint(1, 16))]
        a[0], b[0] = rng.randint(1, 9), rng.randint(1, 9)
        add(a, b, rng.choice([1, len(a) + len(b), rng.randint(1, len(a) + len(b))]))
    return calls


def validate(a, b, k):
    assert 1 <= len(a) <= 500 and 1 <= len(b) <= 500 and 1 <= k <= len(a) + len(b)
    assert all(0 <= x <= 9 for x in a + b) and a[0] != 0 and b[0] != 0
