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

    add("aaabcccd", 2)
    add("aabbaa", 2)
    add("aaaaaaaaaaa", 0)

    for n in [1, 2, 9, 10, 11, 99, 100]:
        for k in [0, 1, n]:
            add("a" * n, k)
    add("ab" * 50, 50)

    while len(calls) < 600:
        n = rng.randint(1, 35)
        mode = len(calls) % 4
        if mode == 0:
            s = rng.choice("abcz") * n
        elif mode == 1:
            s = "".join(rng.choice("abcd") * rng.randint(1, 10) for _ in range(4))[:n]
        else:
            s = "".join(rng.choice("abcd") for _ in range(n))
        add(s, rng.choice([0, len(s), rng.randrange(len(s) + 1)]))
    return calls


def validate(s, k):
    assert 1 <= len(s) <= 100 and 0 <= k <= len(s) and all("a" <= x <= "z" for x in s)
