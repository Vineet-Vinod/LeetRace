def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]])"])
    for index in range(600):
        rows, cols = (
            (1, 100000) if index == 0 else (1 + index % 20, 1 + (index * 7) % 20)
        )
        values = list(range(1, rows * cols + 1))
        permutation = values[:]
        rng.shuffle(permutation)
        mat = [permutation[row * cols : (row + 1) * cols] for row in range(rows)]
        arr = values[:]
        rng.shuffle(arr)
        cases.add(f"candidate(arr={arr!r}, mat={mat!r})")
    return sorted(cases)
