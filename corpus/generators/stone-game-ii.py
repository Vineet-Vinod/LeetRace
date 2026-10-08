def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(piles=[2,7,9,4,4])", "candidate(piles=[1,2,3,4,5,100])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        piles = [rng.randint(1, 10000) for _ in range(n)]
        cases.add(f"candidate(piles={piles!r})")
    return sorted(cases)
