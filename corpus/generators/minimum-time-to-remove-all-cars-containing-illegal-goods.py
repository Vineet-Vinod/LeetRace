import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s = data["s"]
        assert 1 <= len(s) <= 200000 and set(s) <= set("01")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [{"s": "1100101"}, {"s": "0010"}]:
        add(**example)
    add(s="0" * 200000)
    add(s="1" * 200000)
    add(s="01" * 100000)
    while len(calls) < 600:
        n = rng.randint(1, 150)
        mode = len(calls) % 4
        if mode == 0:
            s = "0" * rng.randrange(n) + "1"
            s += "0" * (n - len(s))
        elif mode == 1:
            s = "1" * rng.randrange(n) + "0"
            s += "1" * (n - len(s))
        else:
            s = "".join(rng.choice("01") for _ in range(n))
        add(s=s)
    assert len(calls) == 600
    return calls
