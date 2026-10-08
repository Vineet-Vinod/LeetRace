import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s = kwargs["s"]
        assert 1 <= len(s) <= 200 and set(s) <= set("DI")
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="I" * 200)
    add(s="D" * 200)
    add(s="DI" * 100)
    add(s="DID")
    add(s="D")
    while len(calls) < 600:
        n = rng.randint(1, 35)
        s = "".join(rng.choices("DI", k=n))
        if rng.randrange(4) == 0:
            s = ("DI" * 100)[:n] if rng.randrange(2) else rng.choice("DI") * n
        add(s=s)
    return calls
