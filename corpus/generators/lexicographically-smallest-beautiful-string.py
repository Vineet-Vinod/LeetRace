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

    add("abcz", 26)
    add("dc", 4)

    add(("abc" * 33334)[:100000], 4)
    add(("zyx" * 33334)[:100000], 26)
    add("a", 4)
    add("z", 26)

    while len(calls) < 600:
        k = rng.randint(4, 26)
        n = rng.randint(1, 40)
        mode = len(calls) % 4
        chars = []
        for i in range(n):
            choices = [chr(97 + x) for x in range(k) if chr(97 + x) not in chars[-2:]]
            chars.append(
                choices[-1]
                if mode == 0
                else choices[0]
                if mode == 1
                else rng.choice(choices)
            )
        add("".join(chars), k)
    return calls


def validate(s, k):
    assert 1 <= len(s) <= 100000 and 4 <= k <= 26
    assert all("a" <= c < chr(97 + k) for c in s)
    # Every longer palindrome contains a palindrome of length two or three.
    assert all(
        s[i] != s[i - 1] and (i < 2 or s[i] != s[i - 2]) for i in range(1, len(s))
    )
