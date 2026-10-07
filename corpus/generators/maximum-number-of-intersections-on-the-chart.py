import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(y):
        return (
            2 <= len(y) <= 100000
            and all(1 <= x <= 10**9 for x in y)
            and all(a != b for a, b in zip(y, y[1:]))
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for y in [
        [1, 2, 1, 2, 1, 3, 2],
        [2, 1, 3, 4, 5],
        [1, 10**9] * 50000,
        list(range(1, 100001)),
        [1, 2, 1],
        [2, 1, 2],
    ]:
        emit(y=y)
    while len(calls) < 600:
        y = [rng.randint(1, 30)]
        for _ in range(rng.randint(1, 50)):
            x = rng.randint(1, 30)
            while x == y[-1]:
                x = rng.randint(1, 30)
            y.append(x)
        emit(y=y)
    assert len(calls) == 600
    return list(calls)
