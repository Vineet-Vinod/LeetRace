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

    add([3, 2, 1, 4, 5], 4)
    add([2, 3, 1], 3)

    add(list(range(1, 100001)), 50000)
    add(list(range(100000, 0, -1)), 100000)
    add([1], 1)

    while len(calls) < 600:
        n = rng.randint(2, 45)
        a = list(range(1, n + 1))
        rng.shuffle(a)
        add(a, rng.choice([1, n, rng.randint(1, n)]))
    return calls


def validate(a, k):
    assert 1 <= len(a) <= 100000 and 1 <= k <= len(a)
    assert sorted(a) == list(range(1, len(a) + 1))
