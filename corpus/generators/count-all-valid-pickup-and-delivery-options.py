import random

DOMAIN_SIZE = 500


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    calls: dict[str, None] = {}

    def add(n):
        assert 1 <= n <= 500
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("n", n),))
            + ")"
        )
        calls[call] = None

    add(n=1)
    add(n=2)
    add(n=3)
    for n in range(1, 501):
        add(n=n)
    return list(calls)
