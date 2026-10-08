import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = [
        "candidate(n=1, x=1)",
        "candidate(n=10, x=2)",
        "candidate(n=160, x=3)",
        "candidate(n=300, x=5)",
        "candidate(n=300, x=1)",
    ]
    seen = {(1, 1), (10, 2), (160, 3), (300, 5), (300, 1)}
    while len(cases) < 600:
        n = rng.randint(1, 300)
        x = rng.randint(1, 5)
        key = (n, x)
        if key not in seen:
            seen.add(key)
            assert 1 <= n <= 300 and 1 <= x <= 5
            cases.append(f"candidate(n={n}, x={x})")
    return cases
