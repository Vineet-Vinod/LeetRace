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

    add([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    add([5, 6, 7, 8, 9, 1, 2, 3, 4], 8)
    add([1, 2, 2, 1, 2, 2, 1, 2, 2], 2)

    add([100000] * 10000, 0)
    add([1] * 10000, 9999)
    add([1], 0)

    while len(calls) < 600:
        a = [
            rng.randint(1, rng.choice([10, 100000])) for _ in range(rng.randint(1, 35))
        ]
        add(a, rng.choice([0, len(a) - 1, rng.randrange(len(a))]))
    return calls


def validate(a, k):
    assert 0 <= k < len(a) <= 10000 and all(1 <= x <= 100000 for x in a)
