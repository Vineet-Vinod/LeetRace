import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        n, k = values["n"], values["k"]
        assert 1 <= k <= n <= 1000000000
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for n in [1, 9, 10, 13, 99, 100, 101, 999, 1000, 1000000000]:
        for k in sorted({1, n, max(1, n // 2)}):
            emit(n=n, k=k)
    while len(calls) < 600:
        n = rng.randint(1, 10000) if len(calls) % 2 else rng.randint(1, 1000000000)
        emit(n=n, k=rng.randint(1, n))
    return calls
