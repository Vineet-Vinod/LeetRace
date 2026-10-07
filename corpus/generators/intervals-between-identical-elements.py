def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(arr=[2, 1, 3, 1, 2, 3, 3])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 1000
        distinct = 1 + index % min(size, 50)
        arr = [rng.randint(1, distinct) for _ in range(size)]
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
