import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(stoneValue):
        return 1 <= len(stoneValue) <= 50000 and all(
            -1000 <= x <= 1000 for x in stoneValue
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for a in [
        [1, 2, 3, 7],
        [1, 2, 3, -9],
        [1, 2, 3, 6],
        [1000] * 50000,
        [-1000] * 50000,
        [0] * 50000,
    ]:
        emit(stoneValue=a)
    while len(calls) < 600:
        stoneValue = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 50))]
        if rng.randrange(5) == 0:
            a, b, c = [rng.randint(0, 300) for _ in range(3)]
            stoneValue = [a, b, c, a + b + c]
        emit(stoneValue=stoneValue)
    assert len(calls) == 600
    return list(calls)
