import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    for char in "aA0.!":
        for n in range(1, 51):
            add(password=char * n)
    for n in range(6, 21):
        add(password=("aA0" * 7)[:n])
    add(password="a" * 21 + "B0")
    while len(calls) < 600:
        n = rng.randint(1, 50)
        alphabet = rng.choice(
            (
                "aA0.!",
                "abc",
                "ABC",
                "012",
                "aA0",
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!",
            )
        )
        password = "".join(rng.choice(alphabet) for _ in range(n))
        assert 1 <= len(password) <= 50 and all(
            c.isascii() and (c.isalnum() or c in ".!") for c in password
        )
        add(password=password)
    assert len(calls) == 600
    return list(calls)
