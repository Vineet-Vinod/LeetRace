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

    add([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
    add(
        [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
    )

    add(
        [
            [20000 if r in (0, 199) or c in (0, 199) else 0 for c in range(200)]
            for r in range(200)
        ]
    )
    add([[0] * 200 for _ in range(200)])
    add([[0]])

    while len(calls) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        mode = len(calls) % 4
        if mode == 0:
            rim = rng.randint(1, 20000)
            g = [
                [
                    rim if r in (0, m - 1) or c in (0, n - 1) else rng.randrange(rim)
                    for c in range(n)
                ]
                for r in range(m)
            ]
        elif mode == 1:
            v = rng.randint(0, 20000)
            g = [[v] * n for _ in range(m)]
        else:
            g = [[rng.randint(0, 20000) for _ in range(n)] for _ in range(m)]
        add(g)
    return calls


def validate(g):
    assert (
        1 <= len(g) <= 200
        and 1 <= len(g[0]) <= 200
        and all(len(r) == len(g[0]) for r in g)
    )
    assert all(0 <= x <= 20000 for r in g for x in r)
