import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        matrix = values["matrix"]
        assert (
            1 <= len(matrix) <= 200
            and 1 <= len(matrix[0]) <= 200
            and all(
                len(row) == len(matrix[0]) and all(0 <= x <= 2**31 - 1 for x in row)
                for row in matrix
            )
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(matrix=[[0]])
    emit(matrix=[[2**31 - 1]])
    emit(matrix=[[0] * 200 for _ in range(200)])
    emit(
        matrix=[
            list(range(i * 200, (i + 1) * 200))
            if i % 2 == 0
            else list(range((i + 1) * 200 - 1, i * 200 - 1, -1))
            for i in range(200)
        ]
    )
    while len(calls) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        bound = 3 if len(calls) % 3 == 0 else 1000
        emit(matrix=[[rng.randint(0, bound) for _ in range(n)] for _ in range(m)])
    return calls
