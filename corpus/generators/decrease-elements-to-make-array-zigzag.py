def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[1, 2, 3])", "candidate(nums=[9, 6, 1, 6, 2])"}
    while len(cases) < 600:
        n = rng.randint(1, 50)
        a = [rng.randint(1, 1000) for _ in range(n)]
        cases.add(f"candidate(nums={a!r})")
    return sorted(cases)
