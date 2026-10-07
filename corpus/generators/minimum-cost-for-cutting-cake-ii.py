import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(m=1, n=1, horizontalCut=[], verticalCut=[])
    add(m=100000, n=100000, horizontalCut=[1000] * 99999, verticalCut=[1000] * 99999)
    while len(calls) < 600:
        m, n = rng.randint(1, 25), rng.randint(1, 25)
        h = [rng.randint(1, 1000) for _ in range(m - 1)]
        v = [rng.randint(1, 1000) for _ in range(n - 1)]
        assert (
            len(h) == m - 1 and len(v) == n - 1 and all(1 <= x <= 1000 for x in h + v)
        )
        add(m=m, n=n, horizontalCut=h, verticalCut=v)
    assert len(calls) == 600
    return list(calls)
