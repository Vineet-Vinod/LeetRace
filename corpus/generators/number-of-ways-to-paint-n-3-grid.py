import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(n):
        assert 1 <= n <= 5000
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("n", n),))
            + ")"
        )
        calls[call] = None

    add(n=1)
    add(n=5000)
    add(n=1)
    add(n=5000)
    for n in range(1, 100):
        add(n=n)
    while len(calls) < 600:
        add(n=rng.randint(1, 5000))
    return list(calls)
