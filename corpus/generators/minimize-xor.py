import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(3, 5), (1, 12), (1, 1), (10**9, 10**9)}
    while len(cases) < 600:
        cases.add((rng.randint(1, 10**9), rng.randint(1, 10**9)))
    assert all(1 <= first <= 10**9 and 1 <= second <= 10**9 for first, second in cases)
    return [
        f"candidate(num1={first}, num2={second})" for first, second in sorted(cases)
    ]
