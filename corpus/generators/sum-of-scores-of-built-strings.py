import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(s):
        assert 1 <= len(s) <= 100000 and all("a" <= c <= "z" for c in s)
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("s", s),))
            + ")"
        )
        calls[call] = None

    add(s="babab")
    add(s="azbazbzaz")
    add(s="a" * 100000)
    add(s="ab" * 50000)
    add(s="a" * 99999 + "b")
    while len(calls) < 600:
        n = rng.randint(1, 100)
        mode = rng.randrange(4)
        if mode == 0:
            s = rng.choice("abcdefghijklmnopqrstuvwxyz") * n
        elif mode == 1:
            unit = "".join(rng.choices("abcde", k=rng.randint(1, 8)))
            s = (unit * ((n + len(unit) - 1) // len(unit)))[:n]
        elif mode == 2:
            s = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=n))
        else:
            s = "".join(rng.choices("ab", k=n))
        add(s=s)
    return list(calls)
