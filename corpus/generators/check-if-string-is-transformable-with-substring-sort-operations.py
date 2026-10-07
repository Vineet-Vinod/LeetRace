import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(s, t):
        assert len(s) == len(t) and 1 <= len(s) <= 100000
        assert all(ch in "0123456789" for ch in s + t)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("s", s),
                    ("t", t),
                )
            )
            + ")"
        )
        calls[call] = None

    add(s="84532", t="34852")
    add(s="34521", t="23415")
    add(s="12345", t="12435")
    add(s="9876543210" * 10000, t="".join(sorted("9876543210" * 10000)))
    add(s="0123456789" * 10000, t="9876543210" * 10000)
    add(s="0", t="0")
    add(s="0", t="1")
    while len(calls) < 600:
        n = rng.randint(1, 50)
        s = "".join(rng.choices("0123456789", k=n))
        mode = rng.randrange(4)
        if mode == 0:
            t = "".join(sorted(s))
        elif mode == 1:
            chars = list(s)
            for _ in range(rng.randint(1, 5)):
                a, b = sorted(rng.sample(range(n + 1), 2))
                chars[a:b] = sorted(chars[a:b])
            t = "".join(chars)
        elif mode == 2:
            t = "".join(sorted(s, reverse=True))
        else:
            t = "".join(rng.choices("0123456789", k=n))
        add(s=s, t=t)
    return list(calls)
