import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(s):
        return 1 <= len(s) <= 2000 and all("a" <= c <= "z" for c in s)

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for s in [
        "aab",
        "a",
        "ab",
        "a" * 2000,
        "ab" * 1000,
        ("abcdefghijklmnopqrstuvwxyz" * 77)[:2000],
    ]:
        emit(s=s)
    while len(calls) < 600:
        s = "".join(
            rng.choice(rng.choice(["ab", "abc", "abcdefghijklmnopqrstuvwxyz"]))
            for _ in range(rng.randint(1, 60))
        )
        if rng.randrange(3) == 0:
            s = s + s[::-1]
        emit(s=s)
    assert len(calls) == 600
    return list(calls)
