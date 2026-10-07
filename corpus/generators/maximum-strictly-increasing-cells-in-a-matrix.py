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

    add([[3, 1], [3, 4]])
    add([[1, 1], [1, 1]])
    add([[3, 1, 6], [-9, 5, 7]])

    add([list(range(-100000, 0))])
    add([[100000] for _ in range(100000)])
    add([[0]])

    while len(calls) < 600:
        m, n = rng.randint(1, 9), rng.randint(1, 9)
        mode = len(calls) % 4
        if mode == 0:
            v = rng.randint(-100000, 100000)
            g = [[v] * n for _ in range(m)]
        else:
            g = [
                [
                    rng.randint(-5, 5) if mode == 1 else rng.randint(-100000, 100000)
                    for _ in range(n)
                ]
                for _ in range(m)
            ]
        add(g)
    return calls


def validate(g):
    assert 1 <= len(g) <= 100000 and 1 <= len(g[0]) <= 100000
    assert len(g) * len(g[0]) <= 100000 and all(len(r) == len(g[0]) for r in g)
    assert all(-100000 <= x <= 100000 for r in g for x in r)
