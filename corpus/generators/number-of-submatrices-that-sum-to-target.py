import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        matrix = values["matrix"]
        assert (
            1 <= len(matrix) <= 100
            and 1 <= len(matrix[0]) <= 100
            and all(
                len(row) == len(matrix[0]) and all(-1000 <= x <= 1000 for x in row)
                for row in matrix
            )
        )
        assert -100000000 <= values["target"] <= 100000000
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for matrix, target in [
        ([[0] * 100 for _ in range(100)], 0),
        ([[1000] * 100 for _ in range(100)], 100000000),
        ([[-1000]], -100000000),
        ([[1, -1], [-1, 1]], 0),
        ([[1000]], 1000),
    ]:
        emit(matrix=matrix, target=target)
    while len(calls) < 600:
        m, n = rng.randint(1, 8), rng.randint(1, 8)
        matrix = [[rng.randint(-5, 5) for _ in range(n)] for _ in range(m)]
        target = rng.randint(-100, 100)
        if len(calls) % 2 == 0:
            a, b = sorted(rng.sample(range(m + 1), 2))
            c, d = sorted(rng.sample(range(n + 1), 2))
            target = sum(sum(row[c:d]) for row in matrix[a:b])
        emit(matrix=matrix, target=target)
    return calls
