def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]])",
            "candidate(grid=[[8]])",
        ]
    )
    for index in range(600):
        rows, cols = 1 + index % 10, 1 + (index * 7) % 10
        grid = [[rng.randint(0, 15) for _ in range(cols)] for _ in range(rows)]
        if index % 7 == 0 and rows >= 3 and cols >= 3:
            grid[0][:3] = [4, 3, 8]
            grid[1][:3] = [9, 5, 1]
            grid[2][:3] = [2, 7, 6]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
