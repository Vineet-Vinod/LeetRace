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

    add(1, 1, 3, 5)
    add(1, 1, 2, 2)
    add(1, 1, 1, 1)

    add(1, 1, 1, 10**9)
    add(1, 1, 10**9, 10**9)
    add(10**9, 10**9, 10**9, 10**9)

    while len(calls) < 600:
        sx, sy = rng.randint(1, 100), rng.randint(1, 100)
        if len(calls) % 2:
            tx, ty = sx, sy
            for _ in range(rng.randint(0, 25)):
                if rng.randrange(2):
                    if tx + ty > 10**9:
                        break
                    tx += ty
                else:
                    if tx + ty > 10**9:
                        break
                    ty += tx
        else:
            tx, ty = rng.randint(1, 10**9), rng.randint(1, 10**9)
        add(sx, sy, tx, ty)
    return calls


def validate(sx, sy, tx, ty):
    assert all(1 <= x <= 10**9 for x in (sx, sy, tx, ty))
