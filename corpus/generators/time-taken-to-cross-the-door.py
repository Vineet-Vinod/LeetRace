import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(arrival, state):
        return (
            1 <= len(arrival) <= 100000
            and len(arrival) == len(state)
            and arrival == sorted(arrival)
            and all(0 <= a <= len(arrival) for a in arrival)
            and all(s in (0, 1) for s in state)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(arrival=[0, 1, 1, 2, 4], state=[0, 1, 0, 0, 1])
    emit(arrival=[0, 0, 0], state=[1, 0, 1])
    emit(arrival=[0] * 100000, state=[0, 1] * 50000)
    emit(arrival=list(range(1, 100001)), state=[1, 0] * 50000)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        arrival = sorted(rng.randint(0, n) for _ in range(n))
        state = [rng.randrange(2) for _ in range(n)]
        emit(arrival=arrival, state=state)
    assert len(calls) == 600
    return list(calls)
