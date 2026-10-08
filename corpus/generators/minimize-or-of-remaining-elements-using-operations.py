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

    add([3, 5, 3, 2, 7], 2)
    add([7, 3, 15, 14, 2, 8], 4)
    add([10, 7, 10, 3, 9, 14, 9, 4], 1)

    add([2**30 - 1] * 100000, 99999)
    add([0] * 100000, 0)
    add([0, 2**30 - 1] * 50000, 50000)

    while len(calls) < 600:
        n = rng.randint(1, 35)
        mode = len(calls) % 4
        if mode == 0:
            a = [rng.randint(1, 255) if i % 2 else 0 for i in range(n)]
        else:
            a = [rng.randrange(2 ** rng.choice([3, 10, 30])) for _ in range(n)]
        add(a, rng.choice([0, n - 1, rng.randrange(n)]))
    return calls


def validate(a, k):
    assert 1 <= len(a) <= 100000 and 0 <= k < len(a) and all(0 <= x < 2**30 for x in a)
