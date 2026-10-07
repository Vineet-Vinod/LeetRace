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

    add([1, 2, 3, 4, 5], [1, 2, 3, 4, 6])
    add([2, 3, 2], [2, 2, 3])
    add([3, 4, 3], [4, 3, 2])

    add([1] * 1000, [10**9] * 1000)
    add([10**9] * 1000, [1] * 1000)
    add([1], [1])

    while len(calls) < 600:
        n, m = rng.randint(1, 25), rng.randint(1, 25)
        mode = len(calls) % 4
        a = [rng.randint(1, 20) for _ in range(n)]
        q = [rng.randint(1, 20) for _ in range(m)]
        if mode == 0:
            q = [1] * m
        elif mode == 1:
            q = [10**9] + q[1:]
        elif mode == 2:
            q = sorted(a)[::-1][:m] or [1]
        add(a, q)
    return calls


def validate(a, q):
    assert (
        1 <= len(a) <= 1000
        and 1 <= len(q) <= 1000
        and all(1 <= x <= 10**9 for x in a + q)
    )
