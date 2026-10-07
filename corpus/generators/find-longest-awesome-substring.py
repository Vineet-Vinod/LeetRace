import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s = kwargs["s"]
        assert 1 <= len(s) <= 100000 and set(s) <= set("0123456789")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="3242415")
    add(s="12345678")
    add(s="213123")
    add(s="0" * 100000)
    add(s="0123456789" * 10000)
    add(s="0123456789")
    while len(calls) < 600:
        n = rng.randint(1, 100)
        alphabet = "0123456789"[: rng.randint(1, 10)]
        s = "".join(rng.choices(alphabet, k=n))
        if len(calls) % 4 == 0:
            s = s + s[::-1]
        add(s=s)
    return calls
