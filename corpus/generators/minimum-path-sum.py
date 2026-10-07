def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])"])
    for index in range(600):
        rows, cols = (
            (200, 200) if index == 0 else (1 + index % 20, 1 + (index * 7) % 20)
        )
        grid = [[rng.randint(0, 200) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
