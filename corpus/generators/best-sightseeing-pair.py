def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(values=[1,1])", "candidate(values=[8,1,5,2,6])"}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        a = [rng.randint(1, 1000) for _ in range(n)]
        cases.add(f"candidate(values={a!r})")
    return sorted(cases)
