import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {1, 5, (1 << 31) - 1}
    while len(cases) < 600:
        cases.add(rng.randint(1, (1 << 31) - 1))
    return [f"candidate(num={num})" for num in cases]
