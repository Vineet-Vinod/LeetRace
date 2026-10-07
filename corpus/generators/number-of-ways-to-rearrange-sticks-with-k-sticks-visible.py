import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert 1 <= kw["k"] <= kw["n"] <= 1000
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"n": 3, "k": 2}, {"n": 5, "k": 5}, {"n": 20, "k": 11}] + [
        {"n": 1000, "k": 500},
        {"n": 1000, "k": 1},
        {"n": 1000, "k": 1000},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 250 if len(calls) % 5 in (0, 1) else 80)
        k = rng.randint(1, n)
        if len(calls) % 5 == 0:
            k = 1
        if len(calls) % 5 == 1:
            k = n
        add(n=n, k=k)
    return calls
