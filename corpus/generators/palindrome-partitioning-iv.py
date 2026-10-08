import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(s):
        assert 3 <= len(s) <= 2000 and all("a" <= c <= "z" for c in s)
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("s", s),))
            + ")"
        )
        calls[call] = None

    add(s="abcbdd")
    add(s="bcbddxy")
    add(s="a" * 2000)
    add(s="ab" * 1000)
    add(s=("abcdefghijklmnopqrstuvwxyz" * 77)[:2000])
    while len(calls) < 600:
        mode = rng.randrange(4)
        if mode == 0:
            parts = []
            for _ in range(3):
                half = "".join(rng.choices("abcde", k=rng.randint(1, 10)))
                parts.append(half + half[::-1])
            s = "".join(parts)
        elif mode == 1:
            s = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=rng.randint(6, 70)))
        elif mode == 2:
            s = "".join(rng.choices("ab", k=rng.randint(3, 60)))
        else:
            s = rng.choice("abcdef") * rng.randint(3, 80)
        add(s=s)
    return list(calls)
