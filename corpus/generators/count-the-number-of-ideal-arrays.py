import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(n=10000, maxValue=10000)
    add(n=2, maxValue=10000)
    for n in range(2, 15):
        for v in range(1, 25):
            add(n=n, maxValue=v)
    while len(calls) < 600:
        n, v = rng.randint(2, 10000), rng.randint(1, 250)
        assert 2 <= n <= 10000 and 1 <= v <= 10000
        add(n=n, maxValue=v)
    assert len(calls) == 600
    return list(calls)
