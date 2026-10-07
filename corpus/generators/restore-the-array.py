import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(s, k):
        return (
            1 <= len(s) <= 100000
            and s[0] != "0"
            and s.isascii()
            and s.isdigit()
            and 1 <= k <= 10**9
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for s, k in [
        ("1000", 10000),
        ("1000", 10),
        ("1317", 2000),
        ("1" * 100000, 10**9),
        ("1" + "0" * 99999, 1),
        ("1" * 100000, 1),
    ]:
        emit(s=s, k=k)
    while len(calls) < 600:
        k = rng.choice([1, 9, 10, 100, 1000, 10**9, rng.randint(1, 10000)])
        if rng.randrange(2):
            s = "".join(str(rng.randint(1, k)) for _ in range(rng.randint(1, 12)))
        else:
            s = rng.choice("123456789") + "".join(
                rng.choice("0123456789") for _ in range(rng.randint(0, 50))
            )
        emit(s=s, k=k)
    assert len(calls) == 600
    return list(calls)
