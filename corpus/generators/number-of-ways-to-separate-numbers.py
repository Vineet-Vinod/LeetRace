import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            'candidate(num = "327")',
            'candidate(num = "094")',
            'candidate(num = "0")',
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
        assert 1 <= len(p["num"]) <= 3500 and all("0" <= x <= "9" for x in p["num"])

    add(num="1" * 3500)
    add(num="0" * 3500)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 55)
        s = "".join(rng.choice("0123456789") for _ in range(n))
        if mode < 4:
            s = rng.choice("123456789") + s[1:]
        if mode == 0:
            s = rng.choice("123456789") * n
        add(num=s)
    return list(calls)
