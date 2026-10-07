import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        s, k = kw["s"], kw["k"]
        assert (
            1 <= len(s) <= 50000
            and s.isascii()
            and s.islower()
            and s.isalpha()
            and 1 <= k <= 1000
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"s": "baeyh", "k": 2}, {"s": "abba", "k": 1}, {"s": "bcdf", "k": 1}] + [
        {"s": "ab" * 25000, "k": 1000},
        {"s": "z" * 50000, "k": 1},
        {"s": "ab" * 25000, "k": 1},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        k = rng.randint(1, 1000)
        mode = len(calls) % 4
        if mode == 0:
            k = rng.choice([1, 2, 4, 9, 16, 25])
            s = ("ab" * n)[:n]
        elif mode == 1:
            s = "".join(rng.choice("bcdfgh") for _ in range(n))
        else:
            s = "".join(rng.choice("aeioubcdf") for _ in range(n))
            if mode == 2:
                k = rng.choice([1, 2, 3, 4])
        add(s=s, k=k)
    return calls
