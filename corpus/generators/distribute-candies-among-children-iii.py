import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(n, limit):
        assert 1 <= n <= 100000000 and 1 <= limit <= 100000000
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("n", n),
                    ("limit", limit),
                )
            )
            + ")"
        )
        calls[call] = None

    add(n=5, limit=2)
    add(n=3, limit=3)
    for n in (1, 100000000):
        for limit in (1, 100000000):
            add(n=n, limit=limit)
    while len(calls) < 600:
        limit = rng.randint(1, 100000000) if len(calls) % 5 == 0 else rng.randint(1, 80)
        mode = rng.randrange(4)
        if mode == 0:
            n = min(100000000, 3 * limit + rng.randint(1, 10))
        elif mode == 1:
            n = rng.randint(1, min(limit, 100000000))
        elif mode == 2:
            n = min(100000000, max(1, 3 * limit - rng.randint(0, 10)))
        else:
            n = rng.randint(1, min(100000000, 3 * limit))
        add(n=n, limit=limit)
    return list(calls)
