def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        a, b, c, d = [rng.randint(-100, 100) for _ in range(4)]
        x, y = f"{a}+{b}i", f"{c}+{d}i"
        cases.add(f"candidate(num1={x!r},num2={y!r})")
    return sorted(cases)
