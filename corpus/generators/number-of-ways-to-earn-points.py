import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(target, types):
        return (
            1 <= target <= 1000
            and 1 <= len(types) <= 50
            and all(len(t) == 2 and 1 <= t[0] <= 50 and 1 <= t[1] <= 50 for t in types)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for t in [6, 18]:
        emit(target=t, types=[[6, 1], [3, 2], [2, 3]])
    emit(target=5, types=[[50, 1], [50, 2], [50, 5]])
    emit(target=1000, types=[[50, 50]] * 50)
    emit(target=1000, types=[[50, 1]] * 50)
    while len(calls) < 600:
        types = [
            [rng.randint(1, 12), rng.randint(1, 15)] for _ in range(rng.randint(1, 10))
        ]
        if rng.randrange(2):
            target = sum(rng.randint(0, c) * m for c, m in types)
            target = max(1, target)
        else:
            target = rng.randint(1, 400)
        emit(target=target, types=types)
    assert len(calls) == 600
    return list(calls)
