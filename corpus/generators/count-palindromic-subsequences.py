import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(s):
        return 1 <= len(s) <= 10000 and s.isascii() and s.isdigit()

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for s in [
        "103301",
        "0000000",
        "9999900000",
        "0",
        "0123",
        "9" * 10000,
        "0123456789" * 1000,
    ]:
        emit(s=s)
    while len(calls) < 600:
        n = rng.randint(1, 45)
        alphabet = rng.choice(["0123456789", "01", "3337"])
        s = "".join(rng.choice(alphabet) for _ in range(n))
        if rng.randrange(4) == 0:
            s = s[: n // 2] + s[n // 2 :][::-1] + s[: n // 2][::-1]
        emit(s=s)
    assert len(calls) == 600
    return list(calls)
