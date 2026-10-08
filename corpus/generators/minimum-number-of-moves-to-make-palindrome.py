import random
from collections import Counter


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

    add("aabb")
    add("letelt")

    add("a" * 1000 + "z" * 1000)
    add("ab" * 1000)
    add("a")

    while len(calls) < 600:
        half = "".join(rng.choice("abcdz") for _ in range(rng.randint(0, 20)))
        center = rng.choice("abcdz") if rng.randrange(2) or not half else ""
        s = list(half + center + half[::-1])
        if len(calls) % 4:
            rng.shuffle(s)
        add("".join(s))
    return calls


def validate(s):
    assert 1 <= len(s) <= 2000 and all("a" <= c <= "z" for c in s)
    assert sum(x % 2 for x in Counter(s).values()) <= 1
