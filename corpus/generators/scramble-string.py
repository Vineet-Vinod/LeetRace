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

    add("great", "rgeat")
    add("abcde", "caebd")
    add("a", "a")

    add("abcdefghijklmnopqrstuvwxyzabcd", "dcba" + "zyxwvutsrqponmlkjihgfedcba")
    add("a" * 30, "a" * 29 + "b")
    add("a", "z")

    while len(calls) < 600:
        n = rng.randint(2, 16)
        a = "".join(rng.choice("abcde") for _ in range(n))

        def scramble(s):
            if len(s) == 1:
                return s
            cut = rng.randrange(1, len(s))
            left, right = scramble(s[:cut]), scramble(s[cut:])
            return left + right if rng.randrange(2) else right + left

        mode = len(calls) % 4
        if mode == 0:
            b = scramble(a)
        elif mode == 1:
            b = a[:-1] + "z"
        elif mode == 2:
            chars = list(a)
            rng.shuffle(chars)
            b = "".join(chars)
        else:
            b = a
        add(a, b)
    return calls


def validate(a, b):
    assert 1 <= len(a) == len(b) <= 30 and all("a" <= x <= "z" for x in a + b)
