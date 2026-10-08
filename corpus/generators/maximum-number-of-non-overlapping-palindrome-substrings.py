import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(s, k):
        assert 1 <= k <= len(s) <= 2000
        assert all("a" <= c <= "z" for c in s)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("s", s),
                    ("k", k),
                )
            )
            + ")"
        )
        calls[call] = None

    add(s="abaccdbbd", k=3)
    add(s="adbcda", k=2)
    add(s="a" * 2000, k=1000)
    add(s="a" * 2000, k=1)
    add(s="a" * 1999 + "b", k=2000)
    while len(calls) < 600:
        n = rng.randint(1, 75)
        mode = rng.randrange(4)
        if mode == 0:
            s = rng.choice("abcdef") * n
        elif mode == 1:
            s = "".join(rng.choices("ab", k=n))
        elif mode == 2:
            unit = "".join(rng.choices("abcd", k=rng.randint(1, 5)))
            unit += unit[::-1]
            s = (unit * ((n + len(unit) - 1) // len(unit)))[:n]
        else:
            s = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=n))
        k = rng.randint(1, n)
        add(s=s, k=k)
    return list(calls)
