import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: num1,num2 in [-100,100]."""
    rng = random.Random(seed)
    cases = {(a, b) for a in range(-10, 11) for b in range(-10, 11)}
    cases.update(
        {(-100, 100), (100, -100), (-100, -100), (100, 100), (0, 0), (12, 5), (-10, 4)}
    )
    while len(cases) < 600:
        cases.add((rng.randint(-100, 100), rng.randint(-100, 100)))
    return [f"candidate(num1={a}, num2={b})" for a, b in sorted(cases)]
