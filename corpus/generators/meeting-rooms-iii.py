import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(n, meetings):
        return (
            1 <= n <= 100
            and 1 <= len(meetings) <= 100000
            and len({s for s, e in meetings}) == len(meetings)
            and all(0 <= s < e <= 500000 for s, e in meetings)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(n=100, meetings=[[499999, 500000]])
    emit(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]])
    emit(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]])
    emit(n=100, meetings=[[i, 500000] for i in range(100000)])
    emit(n=1, meetings=[[i, i + 1] for i in range(100000)])
    while len(calls) < 600:
        n = rng.randint(1, 10)
        starts = rng.sample(range(200), rng.randint(1, 40))
        meetings = [[s, s + rng.randint(1, 200)] for s in starts]
        emit(n=n, meetings=meetings)
    assert len(calls) == 600
    return list(calls)
