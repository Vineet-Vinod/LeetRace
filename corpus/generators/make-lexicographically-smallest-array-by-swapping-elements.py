def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[1],limit=1)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(1, 1000) for _ in range(n)]
        limit = rng.randint(1, 1000)
        cases.add(f"candidate(nums={nums!r},limit={limit})")
    return sorted(cases)
