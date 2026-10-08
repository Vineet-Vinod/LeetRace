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

    add([8, 7, 3, 5, 7, 2, 4, 9])
    add([8, 10, 3, 8, 1, 13, 7, 9, 4])

    add([10**9] * 10000)
    add([1] * 10000)
    add([1])

    while len(calls) < 600:
        a = [rng.randint(1, rng.choice([10, 10**9])) for _ in range(rng.randint(1, 70))]
        add(a)
    return calls


def validate(a):
    assert 1 <= len(a) <= 10000 and all(1 <= x <= 10**9 for x in a)
