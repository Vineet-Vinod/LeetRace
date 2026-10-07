import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            'candidate(s = "abcd", t = "cdab", k = 2)',
            'candidate(s = "ababab", t = "ababab", k = 1)',
        ]
    )

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        calls[ast.unparse(ast.parse(call, mode="eval"))] = None

    def validate(p):
        assert 2 <= len(p["s"]) <= 500000 and len(p["s"]) == len(p["t"])
        assert all("a" <= c <= "z" for c in p["s"] + p["t"]) and 1 <= p["k"] <= 10**15

    add(s="a" * 500000, t="a" * 500000, k=10**15)
    add(s="ab" * 250000, t="ba" * 250000, k=1)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(2, 70)
        s = "".join(rng.choice("abcde") for _ in range(n))
        if mode == 0:
            s = rng.choice("abc") * n
        if mode == 1:
            s = "ab" * (n // 2)
            n = len(s)
        if mode < 6:
            shift = rng.randrange(n)
            t = s[shift:] + s[:shift]
        else:
            t = "".join(rng.choice("abcde") for _ in range(n))
        add(s=s, t=t, k=rng.choice([1, 2, 3, 10**15, rng.randint(1, 1000)]))
    return list(calls)
