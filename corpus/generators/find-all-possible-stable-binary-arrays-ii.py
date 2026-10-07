import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(zero, one, limit):
        assert 1 <= zero <= 1000 and 1 <= one <= 1000 and 1 <= limit <= 1000
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("zero", zero),
                    ("one", one),
                    ("limit", limit),
                )
            )
            + ")"
        )
        calls[call] = None

    add(zero=1, one=1, limit=2)
    add(zero=1, one=2, limit=1)
    add(zero=3, one=3, limit=2)
    add(zero=1000, one=1000, limit=1000)
    add(zero=1000, one=1000, limit=1)
    add(zero=1000, one=1, limit=1000)
    add(zero=1, one=1000, limit=1)
    while len(calls) < 600:
        zero, one = rng.randint(1, 20), rng.randint(1, 20)
        limit = 1 if len(calls) % 4 == 0 else rng.randint(1, 30)
        if len(calls) % 4 == 1:
            one = zero + rng.randint(-1, 1)
            one = max(1, one)
        add(zero=zero, one=one, limit=limit)
    return list(calls)
