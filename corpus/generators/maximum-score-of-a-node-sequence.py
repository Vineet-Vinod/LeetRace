import random
import itertools


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(scores, edges):
        n = len(scores)
        pairs = [tuple(sorted(e)) for e in edges]
        return (
            4 <= n <= 50000
            and all(1 <= x <= 10**8 for x in scores)
            and len(edges) <= 50000
            and len(set(pairs)) == len(pairs)
            and all(
                len(e) == 2 and 0 <= e[0] < n and 0 <= e[1] < n and e[0] != e[1]
                for e in edges
            )
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(scores=[5, 2, 9, 8, 4], edges=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
    emit(
        scores=[10**8] * 50000, edges=[[i, i + 1] for i in range(49999)] + [[0, 49999]]
    )
    emit(scores=[1] * 50000, edges=[])
    while len(calls) < 600:
        n = rng.randint(4, 18)
        scores = [rng.randint(1, 100) for _ in range(n)]
        if rng.randrange(3) == 0:
            edges = [[0, i] for i in range(1, n)]
        else:
            edges = [
                list(e)
                for e in itertools.combinations(range(n), 2)
                if rng.random() < 0.25
            ]
        emit(scores=scores, edges=edges)
    assert len(calls) == 600
    return list(calls)
