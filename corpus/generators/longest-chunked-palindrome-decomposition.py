import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            'candidate(text = "ghiabcdefhelloadamhelloabcdefghi")',
            'candidate(text = "merchant")',
            'candidate(text = "antaprezatepzapreanta")',
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
        assert 1 <= len(p["text"]) <= 1000 and all("a" <= c <= "z" for c in p["text"])

    add(text="a" * 1000)
    add(text="a" * 500 + "b" * 500)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 70)
        s = "".join(rng.choice("abcde") for _ in range(n))
        if mode < 4:
            pieces = [
                "".join(rng.choice("abc") for _ in range(rng.randint(1, 5)))
                for _ in range(rng.randint(1, 6))
            ]
            s = "".join(pieces) + s + "".join(pieces[::-1])
        add(text=s)
    return list(calls)
