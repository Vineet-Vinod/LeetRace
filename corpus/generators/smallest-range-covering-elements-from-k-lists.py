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

    add([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    add([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    add([list(range(-100000, -99950)) for _ in range(3500)])
    add([[-100000], [100000]])
    add([[0]])

    while len(calls) < 600:
        a = [
            sorted(rng.randint(-100000, 100000) for _ in range(rng.randint(1, 12)))
            for _ in range(rng.randint(1, 10))
        ]
        if len(calls) % 4 == 0:
            common = rng.randint(-10, 10)
            a = [sorted(r + [common]) for r in a]
        add(a)
    return calls


def validate(a):
    assert 1 <= len(a) <= 3500
    assert all(
        1 <= len(r) <= 50 and sorted(r) == r and all(-100000 <= x <= 100000 for x in r)
        for r in a
    )
