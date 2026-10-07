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

    add([2, 3, 5], [[4, 8], [2, 8]])
    add([2, 3, 5], [[1, 4], [2, 3], [3, 4]])
    add([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]])

    add([1] * 100000, [[100000]])
    add([100000], [list(range(1, 100001))])
    add([100000], [[1] for _ in range(100000)])
    add([1], [[1]])

    while len(calls) < 600:
        p = [rng.randint(1, 100) for _ in range(rng.randint(1, 25))]
        b = [
            rng.sample(range(1, 101), rng.randint(1, 12))
            for _ in range(rng.randint(1, 8))
        ]
        mode = len(calls) % 4
        if mode == 0:
            b = [sorted(set(p))] + b
        elif mode == 1:
            p[-1] = 100000
        elif mode == 2:
            b[0] = sorted(set(b[0] + [100]))
        add(p, b)
    return calls


def validate(p, b):
    assert 1 <= len(p) <= 100000 and 1 <= len(b) <= 100000
    assert all(1 <= x <= 100000 for x in p)
    assert sum(map(len, b)) <= 100000
    assert all(
        1 <= len(r) <= 100000
        and len(r) == len(set(r))
        and all(1 <= x <= 100000 for x in r)
        for r in b
    )
