def generate(seed: int = 0) -> list[str]:
    import random
    import math

    rng = random.Random(seed)
    cases = {"candidate(num='123',k=1)"}
    while len(cases) < 600:
        n = rng.randint(3, 9)
        digits = rng.sample("123456789", n)
        num = "".join(sorted(digits))
        k = rng.randint(1, min(10, math.factorial(n) - 1))
        cases.add(f"candidate(num={num!r},k={k})")
    return sorted(cases)
