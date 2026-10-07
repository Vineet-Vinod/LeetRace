def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])"
        ]
    )
    for index in range(600):
        rows, cols = (
            (200, 200) if index == 0 else (1 + index % 20, 1 + (index * 7) % 20)
        )
        heights = [[rng.randint(0, 100000) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(heights={heights!r})")
    return sorted(cases)
