import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    for s in (
        "0",
        "e",
        ".",
        "2",
        "0089",
        "-0.1",
        "+3.14",
        "4.",
        "-.9",
        "2e10",
        "-90E3",
        "3e+7",
        "+6e-1",
        "53.5e93",
        "-123.456e789",
        "abc",
        "1a",
        "1e",
        "e3",
        "99e2.5",
        "--6",
        "-+3",
        "95a54e53",
        "9" * 20,
    ):
        add(s=s)
    while len(calls) < 600:

        def digits() -> str:
            return "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 5)))

        if len(calls) % 2 == 0:
            s = rng.choice(("", "+", "-")) + rng.choice(
                (digits(), digits() + ".", digits() + "." + digits(), "." + digits())
            )
            if rng.randrange(2):
                s += rng.choice(("e", "E")) + rng.choice(("", "+", "-")) + digits()
        else:
            # Guaranteed invalid alphabetic suffix other than exponent notation.
            s = "".join(
                rng.choice("0123456789+-.eE") for _ in range(rng.randint(1, 18))
            ) + rng.choice("aBz")
        if len(s) > 20:
            continue
        assert 1 <= len(s) <= 20 and all(
            c.isascii() and (c.isalnum() or c in "+-.") for c in s
        )
        add(s=s)
    assert len(calls) == 600
    return list(calls)
