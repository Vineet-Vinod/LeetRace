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

    add(3, 3, 1)
    add(2, 3, 0)
    add(2, 3, 1)

    add(100, 100, 99)
    add(1, 100, 0)
    add(1, 1, 0)
    add(50, 100, 0)

    while len(calls) < 600:
        n = rng.randint(1, 35)
        add(n, rng.randint(n, 100), rng.choice([0, n - 1, rng.randrange(n)]))
    return calls


def validate(n, goal, k):
    assert 0 <= k < n <= goal <= 100
