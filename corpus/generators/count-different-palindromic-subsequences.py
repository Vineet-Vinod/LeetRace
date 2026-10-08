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

    add("bccb")
    add("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba")

    add("a" * 1000)
    add("abcd" * 250)
    add("d")

    while len(calls) < 600:
        n = rng.randint(1, 40)
        s = "".join(rng.choice("abcd"[: rng.randint(1, 4)]) for _ in range(n))
        add(s)
    return calls


def validate(s):
    assert 1 <= len(s) <= 1000 and set(s) <= set("abcd")
