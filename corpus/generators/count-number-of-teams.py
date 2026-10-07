def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(rating=[2, 5, 3, 4, 1])", "candidate(rating=[1, 2, 3])"])
    for index in range(600):
        size = 1000 if index % 100 == 0 else 3 + index % 98
        rating = rng.sample(range(1, 100001), size)
        cases.add(f"candidate(rating={rating!r})")
    while len(cases) < 600:
        rating = rng.sample(range(1, 100001), rng.randint(3, 80))
        cases.add(f"candidate(rating={rating!r})")
    return sorted(cases)
