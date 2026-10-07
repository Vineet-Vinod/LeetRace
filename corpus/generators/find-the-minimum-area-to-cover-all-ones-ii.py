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

    add([[1, 0, 1], [1, 1, 1]])
    add([[1, 0, 1, 0], [0, 1, 0, 1]])

    add([[1] * 30 for _ in range(30)])
    add([[1] * 30])
    add([[1] for _ in range(30)])
    add(
        [
            [int((r, c) in ((0, 0), (0, 29), (29, 0))) for c in range(30)]
            for r in range(30)
        ]
    )

    while len(calls) < 600:
        m, n = rng.randint(1, 6), rng.randint(1, 6)
        if m * n < 3:
            continue
        ones = set(rng.sample(range(m * n), rng.randint(3, m * n)))
        add([[int(r * n + c in ones) for c in range(n)] for r in range(m)])
    return calls


def validate(g):
    assert (
        1 <= len(g) <= 30
        and 1 <= len(g[0]) <= 30
        and all(len(r) == len(g[0]) for r in g)
    )
    assert all(x in (0, 1) for r in g for x in r) and sum(map(sum, g)) >= 3
