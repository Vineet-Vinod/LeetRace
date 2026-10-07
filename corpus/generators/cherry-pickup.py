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

    add([[0, 1, -1], [1, 0, -1], [1, 1, 1]])
    add([[1, 1, -1], [1, -1, 1], [-1, 1, 1]])

    add([[1] * 50 for _ in range(50)])
    add([[0]])
    add([[1]])
    add([[0, -1], [-1, 1]])

    while len(calls) < 600:
        n = rng.randint(2, 9)
        mode = len(calls) % 4
        g = [
            [
                rng.choice([-1, 0, 1]) if mode == 0 else rng.randint(0, 1)
                for _ in range(n)
            ]
            for _ in range(n)
        ]
        g[0][0] = rng.randint(0, 1)
        g[-1][-1] = rng.randint(0, 1)
        if mode == 1:
            if n == 2:
                g[0][1] = g[1][0] = -1
            else:
                for c in range(n):
                    g[n // 2][c] = -1
        elif mode == 2:
            for r in range(n):
                for c in range(n):
                    if rng.random() < 0.3 and r != 0 and c != n - 1:
                        g[r][c] = -1
        add(g)
    return calls


def validate(g):
    assert 1 <= len(g) <= 50 and all(len(r) == len(g) for r in g)
    assert all(x in (-1, 0, 1) for r in g for x in r)
    assert g[0][0] != -1 and g[-1][-1] != -1
