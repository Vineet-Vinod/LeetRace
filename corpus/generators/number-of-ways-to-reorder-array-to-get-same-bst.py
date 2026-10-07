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

    add([2, 1, 3])
    add([3, 4, 5, 1, 2])
    add([1, 2, 3])

    add(list(range(1, 1001)))
    add(list(range(1000, 0, -1)))
    a = list(range(1, 1001))
    rng.shuffle(a)
    add(a)
    add([1])

    while len(calls) < 600:
        n = rng.randint(2, 200) if len(calls) % 5 == 0 else rng.randint(2, 35)
        a = list(range(1, n + 1))
        if len(calls) % 5:
            rng.shuffle(a)
        else:
            a.reverse()
        add(a)
    return calls


def validate(a):
    assert 1 <= len(a) <= 1000 and sorted(a) == list(range(1, len(a) + 1))
