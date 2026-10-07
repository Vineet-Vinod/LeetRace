import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        assert 1 <= kwargs["n"] <= 10**9
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for n in [1, 2, 3, 4, 10, 10**9]:
        add(n=n)
    add(n=3)
    add(n=4)
    add(n=10)
    while len(calls) < 600:
        h = rng.randint(1, 1800)
        n = rng.choice(
            [
                rng.randint(1, 10**9),
                max(1, h * (h + 1) * (h + 2) // 6 + rng.randint(-2, 2)),
            ]
        )
        add(n=n)
    return calls
