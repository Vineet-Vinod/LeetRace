import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        assert (
            1 <= kwargs["n"] <= 10**9
            and 2 <= kwargs["a"] <= 40000
            and 2 <= kwargs["b"] <= 40000
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=10**9, a=40000, b=39999)
    add(n=1, a=2, b=2)
    add(n=1, a=2, b=3)
    add(n=4, a=2, b=3)
    while len(calls) < 600:
        n = rng.choice([rng.randint(1, 100), rng.randint(1, 10**9)])
        a = rng.randint(2, 40000)
        b = rng.choice([a, rng.randint(2, 40000)])
        add(n=n, a=a, b=b)
    return calls
