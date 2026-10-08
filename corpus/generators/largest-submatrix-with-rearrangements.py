def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]])"])
    for index in range(600):
        rows, cols = (
            (100, 100) if index == 0 else (1 + index % 20, 1 + (index * 7) % 20)
        )
        matrix = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(matrix={matrix!r})")
    return sorted(cases)
