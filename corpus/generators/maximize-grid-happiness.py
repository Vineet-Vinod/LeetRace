import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        m, n, i, e = (
            kwargs["m"],
            kwargs["n"],
            kwargs["introvertsCount"],
            kwargs["extrovertsCount"],
        )
        assert (
            1 <= m <= 5
            and 1 <= n <= 5
            and 0 <= i <= min(m * n, 6)
            and 0 <= e <= min(m * n, 6)
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(m=5, n=5, introvertsCount=6, extrovertsCount=6)
    add(m=1, n=1, introvertsCount=0, extrovertsCount=0)
    add(m=2, n=3, introvertsCount=1, extrovertsCount=2)
    add(m=3, n=1, introvertsCount=2, extrovertsCount=1)
    add(m=2, n=2, introvertsCount=4, extrovertsCount=0)
    while len(calls) < 600:
        m = rng.randint(1, 5)
        n = rng.randint(1, 5)
        limit = min(m * n, 6)
        add(
            m=m,
            n=n,
            introvertsCount=rng.randint(0, limit),
            extrovertsCount=rng.randint(0, limit),
        )
    return calls
