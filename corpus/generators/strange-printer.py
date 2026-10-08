import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert (
            1 <= len(kw["s"]) <= 100
            and kw["s"].isascii()
            and kw["s"].isalpha()
            and kw["s"].islower()
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"s": "aaabbb"}, {"s": "aba"}] + [
        {"s": "ab" * 50},
        {"s": "a" * 100},
        {"s": ("abcdefghijklmnopqrstuvwxyz" * 4)[:100]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 22)
        s = "".join(rng.choice("abcde") for _ in range(n))
        if len(calls) % 3 == 0:
            s = s + s[::-1]
        if len(calls) % 3 == 1:
            s = "".join(c * rng.randint(1, 3) for c in s)
        add(s=s)
    return calls
