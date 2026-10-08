import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        assert all(
            1 <= len(args[key]) <= 100000
            and set(args[key]) <= set("abcdefghijklmnopqrstuvwxyz")
            for key in ("s", "t")
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(s="abacaba", t="bzaa")
    add(s="cde", t="xyz")
    add(s="a" * 100000, t="a" * 100000)
    add(s="a" * 100000, t="b" * 100000)
    add(s="ab" * 50000, t="a" * 50000 + "z" + "b" * 49999)
    add(s="abacaba", t="bzaa")
    add(s="cde", t="xyz")
    while len(calls) < 600:
        s = "".join(rng.choices("abc", k=rng.randint(1, 60)))
        kind = len(calls) % 3
        if kind == 0:
            indices = sorted(rng.sample(range(len(s)), rng.randint(1, len(s))))
            t = "".join(s[i] for i in indices)
        elif kind == 1:
            indices = sorted(rng.sample(range(len(s)), rng.randint(1, len(s))))
            t = "".join(s[i] for i in indices)
            pos = rng.randrange(len(t) + 1)
            t = t[:pos] + "z" * rng.randint(1, 10) + t[pos:]
        else:
            t = "".join(rng.choices("abcd", k=rng.randint(1, 60)))
        add(s=s, t=t)
    return list(calls)[:600]
