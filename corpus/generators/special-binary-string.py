import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s = kwargs["s"]
        balance = 0
        assert 1 <= len(s) <= 50 and set(s) <= set("01")
        for ch in s:
            balance += 1 if ch == "1" else -1
            assert balance >= 0
        assert balance == 0
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="1" * 25 + "0" * 25)
    add(s="10" * 25)
    add(s="11011000")
    add(s="10")
    while len(calls) < 600:
        pairs = rng.randint(1, 25)
        opened = closed = 0
        chars = []
        while closed < pairs:
            if opened < pairs and (opened == closed or rng.randrange(2)):
                chars.append("1")
                opened += 1
            else:
                chars.append("0")
                closed += 1
        add(s="".join(chars))
    return calls
