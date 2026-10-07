import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((2, 7, 4, 3), 4), ((2, 5, 3, 4), 7), ((3, 3, 3), 0)}
    while len(cases) < 600:
        damage = tuple(rng.randint(0, 100000) for _ in range(rng.randint(1, 100)))
        cases.add((damage, rng.randint(0, 100000)))
    return [
        f"candidate(damage={list(damage)!r}, armor={armor})" for damage, armor in cases
    ]
