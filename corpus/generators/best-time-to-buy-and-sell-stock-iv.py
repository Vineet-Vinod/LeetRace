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

    add(2, [2, 4, 1])
    add(2, [3, 2, 6, 5, 0, 3])

    add(100, [0, 1000] * 500)
    add(1, [1000] * 1000)
    add(1, [0])

    while len(calls) < 600:
        n = rng.randint(1, 35)
        a = [rng.randint(0, 1000) for _ in range(n)]
        if len(calls) % 4 == 0:
            a.sort(reverse=bool(len(calls) % 8))
        add(rng.randint(1, 100), a)
    return calls


def validate(k, a):
    assert 1 <= k <= 100 and 1 <= len(a) <= 1000
    assert all(0 <= x <= 1000 for x in a)
