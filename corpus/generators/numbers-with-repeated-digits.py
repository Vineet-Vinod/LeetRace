import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    for n in range(1, 201):
        add(n=n)
    for power in range(1, 10):
        for delta in (-1, 0, 1):
            n = 10**power + delta
            if 1 <= n <= 10**9:
                add(n=n)
    while len(calls) < 600:
        n = rng.randint(1, 10 ** rng.randint(2, 9))
        assert 1 <= n <= 10**9
        add(n=n)
    assert len(calls) == 600
    return list(calls)
