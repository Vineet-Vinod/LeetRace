import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        s = d["s"]
        assert len(s) <= 30000 and set(s) <= set("()")

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="(()")
    add(s=")()())")
    add(s="")
    add(s="(" * 15000 + ")" * 15000)
    add(s=")" * 30000)
    add(s="()" * 15000)
    t = 0
    while len(calls) < 600:
        n = rng.randint(0, 100)
        s = "".join(rng.choice("()") for _ in range(n))
        if t % 4 == 0:
            s = "(" * rng.randint(1, 30) + ")" * rng.randint(1, 30)
        add(s=s)
        t += 1
    return calls
