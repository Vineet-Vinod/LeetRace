def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[5])"}
    while len(cases) < 600:
        n = rng.randint(1, 300)
        a = [rng.randint(0, 9) for _ in range(n)]
        cases.add(f"candidate(nums={a!r})")
    return sorted(cases)
