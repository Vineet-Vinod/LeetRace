def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(n=1,k=6,target=3)"}
    while len(cases) < 600:
        n, k = rng.randint(1, 30), rng.randint(1, 30)
        target = rng.randint(1, 1000)
        cases.add(f"candidate(n={n},k={k},target={target})")
    return sorted(cases)
