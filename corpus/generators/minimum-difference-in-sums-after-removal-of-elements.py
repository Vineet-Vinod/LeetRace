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

    add([3, 1, 2])
    add([7, 9, 5, 8, 1, 3])

    add([100000] * 300000)
    add([100000] * 100000 + [1] * 100000 + [100000] * 100000)
    add([1, 1, 1])

    while len(calls) < 600:
        n = rng.randint(1, 20)
        a = [rng.randint(1, 100000) for _ in range(3 * n)]
        if len(calls) % 3 == 0:
            a.sort(reverse=bool(len(calls) % 2))
        add(a)
    return calls


def validate(a):
    assert (
        len(a) % 3 == 0
        and 1 <= len(a) // 3 <= 100000
        and all(1 <= x <= 100000 for x in a)
    )
