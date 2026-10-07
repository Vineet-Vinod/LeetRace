def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(mat=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]])",
        f"candidate(mat={[[1] * 10000]!r})",
        f"candidate(mat={[[1] for _ in range(10000)]!r})",
        f"candidate(mat={[[0] * 10000]!r})",
        f"candidate(mat={[[0] for _ in range(10000)]!r})",
    }
    # The stated limits allow either dimension to reach 10,000 when the other is 1.
    for index in range(600):
        rows, cols = (
            (100, 100) if index == 0 else (1 + index % 20, 1 + (index * 7) % 20)
        )
        mat = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(mat={mat!r})")
    return sorted(cases)
