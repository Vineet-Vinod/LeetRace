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

    add([2, 1, -2, 5], [3, 0, -6])
    add([3, -2], [2, -6, 7])
    add([-1, -1], [1, 1])

    add([-1000] * 500, [1000] * 500)
    add([1000] * 500, [1000] * 500)
    add([0], [-1000])

    while len(calls) < 600:
        mode = len(calls) % 4
        a = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 25))]
        b = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 25))]
        if mode == 0:
            a, b = [abs(x) + (x == 0) for x in a], [-abs(x) - (x == 0) for x in b]
        if mode == 1:
            a = [0] * len(a)
        add(a, b)
    return calls


def validate(a, b):
    assert 1 <= len(a) <= 500 and 1 <= len(b) <= 500
    assert all(-1000 <= x <= 1000 for x in a + b)
