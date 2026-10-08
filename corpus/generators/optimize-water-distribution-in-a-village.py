import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        n, wells, pipes = values["n"], values["wells"], values["pipes"]
        assert (
            2 <= n <= 10000 and len(wells) == n and all(0 <= c <= 100000 for c in wells)
        )
        assert 1 <= len(pipes) <= 10000 and all(
            len(p) == 3
            and 1 <= p[0] <= n
            and 1 <= p[1] <= n
            and p[0] != p[1]
            and 0 <= p[2] <= 100000
            for p in pipes
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(n=2, wells=[0, 0], pipes=[[1, 2, 0]])
    emit(
        n=10000,
        wells=[100000] * 10000,
        pipes=[[i, i + 1, 0] for i in range(1, 10000)] + [[1, 10000, 100000]],
    )
    emit(n=3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]])
    while len(calls) < 600:
        n = rng.randint(2, 30)
        pipes = []
        for _ in range(rng.randint(1, 80)):
            a, b = rng.sample(range(1, n + 1), 2)
            pipes.append([a, b, rng.randint(0, 100)])
        emit(n=n, wells=[rng.randint(0, 100) for _ in range(n)], pipes=pipes)
    return calls
