def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(heights=[2,1,1,2,1,2,2],volume=4,k=3)"}
    while len(cases) < 600:
        n = rng.randint(1, 30)
        heights = [rng.randint(0, 20) for _ in range(n)]
        volume = rng.randint(1, 100)
        k = rng.randrange(n)
        cases.add(f"candidate(heights={heights!r},volume={volume},k={k})")
    return sorted(cases)
