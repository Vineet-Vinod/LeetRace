import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s = kwargs["s"]
        assert 1 <= len(s) <= 100000 and s.isascii() and s.isalpha() and s.islower()
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="a" * 100000)
    add(s="a" * 99999 + "b")
    add(s="level")
    add(s="ababab")
    while len(calls) < 600:
        n = rng.randint(1, 150)
        mode = len(calls) % 4
        if mode == 0:
            base = "".join(rng.choices("abc", k=rng.randint(1, 15)))
            s = (base * 150)[:n]
        elif mode == 1:
            base = "".join(rng.choices("abc", k=rng.randint(1, 30)))
            s = base + "xyz" + base
        else:
            s = "".join(rng.choices("abcdefghijklmnopqrstuvwxyz", k=n))
        add(s=s)
    return calls
