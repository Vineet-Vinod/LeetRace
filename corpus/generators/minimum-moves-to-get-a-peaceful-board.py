def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(rooks=[[0, 0], [1, 0], [1, 1]])"])
    for index in range(600):
        size = 500 if index == 0 else 1 + index % 100
        cells = rng.sample(range(size * size), size)
        rooks = [[cell // size, cell % size] for cell in cells]
        cases.add(f"candidate(rooks={rooks!r})")
    return sorted(cases)
