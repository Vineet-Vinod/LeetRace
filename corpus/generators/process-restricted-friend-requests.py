import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(n, restrictions, requests):
        return (
            2 <= n <= 1000
            and 0 <= len(restrictions) <= 1000
            and 1 <= len(requests) <= 1000
            and all(
                len(e) == 2 and 0 <= e[0] < n and 0 <= e[1] < n and e[0] != e[1]
                for e in restrictions + requests
            )
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(n=3, restrictions=[[0, 1]], requests=[[0, 2], [2, 1]])
    emit(
        n=1000,
        restrictions=[[0, 999]] * 1000,
        requests=[[i, i + 1] for i in range(999)] + [[0, 999]],
    )
    emit(
        n=1000, restrictions=[], requests=[[i, i + 1] for i in range(999)] + [[0, 999]]
    )
    while len(calls) < 600:
        n = rng.randint(2, 20)
        restrictions = [rng.sample(range(n), 2) for _ in range(rng.randint(0, 30))]
        requests = [rng.sample(range(n), 2) for _ in range(rng.randint(1, 40))]
        emit(n=n, restrictions=restrictions, requests=requests)
    assert len(calls) == 600
    return list(calls)
